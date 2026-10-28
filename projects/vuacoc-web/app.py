"""VuaCoc Web Arena Server - Backend Python phuc vu dau truong Vua Coc.
Chay 100% bang thu vien chuan cua Python (http.server, json, urllib, pathlib, random).
Khong can cai dat them framework ngoai (zero-dependency).
Ho tro ca 2 che do:
1. 1D Line Arena (Chuan giao trinh Python Journey)
2. 2D Lotus Pond Arena (Dam sen dai chien 5x5 voi ruoi vang, da ngam va Smart AI)
"""

from __future__ import annotations

import json
import mimetypes
import random
import sys
import traceback
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

# Ket noi voi local_arena cua vuacoc-bot-journey
REPO_ROOT = Path(__file__).resolve().parents[2]
VUACOC_DIR = REPO_ROOT / "projects" / "vuacoc-bot-journey"
if str(VUACOC_DIR) not in sys.path:
    sys.path.insert(0, str(VUACOC_DIR))

from baselines.cautious_bot import choose_action as cautious_action  # noqa: E402
from baselines.forward_bot import choose_action as forward_action  # noqa: E402
from baselines.wait_bot import choose_action as wait_action  # noqa: E402
from local_arena.arena import (  # noqa: E402
    DEFAULT_MAX_TURNS,
    MAX_POSITION,
    MIN_POSITION,
    bot_view,
    initial_state,
    run_match,
    transition,
)
from local_arena.tournament import evaluate_bot, summarize_results  # noqa: E402
from student_bot.bot import choose_action as student_action  # noqa: E402

STATIC_DIR = Path(__file__).resolve().parent / "static"

BOT_REGISTRY = {
    "student": {
        "name": "Student Bot",
        "desc": "Bot của học viên với chiến thuật thông minh, né va chạm và tiến về đích.",
        "fn": student_action,
    },
    "forward": {
        "name": "Forward Bot",
        "desc": "Luôn tiến thẳng về đích, không quan tâm đối thủ.",
        "fn": forward_action,
    },
    "cautious": {
        "name": "Cautious Bot",
        "desc": "Tiến về đích nhưng dừng chờ nếu đối thủ ở cự ly gần (<= 1).",
        "fn": cautious_action,
    },
    "wait": {
        "name": "Wait Bot",
        "desc": "Luôn đứng yên tại chỗ.",
        "fn": wait_action,
    },
}


def create_custom_bot(code: str):
    """Biên dịch mã code Python tự viết của người dùng thành hàm choose_action."""
    if not code or not code.strip():
        return None, "Mã code trống."
    scope: dict = {}
    try:
        compiled = compile(code, "<custom_bot>", "exec")
        exec(compiled, scope)
    except Exception as e:
        return None, f"Lỗi cú pháp Python: {e}"
    if "choose_action" not in scope or not callable(scope["choose_action"]):
        return None, "Thiếu hàm choose_action(state)."
    return scope["choose_action"], None


# ==============================================================================
# 2D POND ARENA ENGINE & SMART AI
# ==============================================================================
GRID_SIZE = 5
ACTIONS_2D = ("up", "down", "left", "right", "wait")
DELTAS_2D = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
    "wait": (0, 0),
}


def create_2d_game(grid_size: int = GRID_SIZE, num_rocks: int = 3, num_flies: int = 3) -> dict:
    """Sinh ban co 2D moi voi ruoi vang va da ngam ngau nhien."""
    occupied = {(0, 0), (grid_size - 1, grid_size - 1)}

    # Sinh da ngam (obstacles)
    rocks = []
    while len(rocks) < num_rocks:
        rx, ry = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
        if (rx, ry) not in occupied:
            occupied.add((rx, ry))
            rocks.append({"x": rx, "y": ry})

    # Sinh ruoi vang (bonus points)
    flies = []
    while len(flies) < num_flies:
        fx, fy = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
        if (fx, fy) not in occupied:
            occupied.add((fx, fy))
            flies.append({"x": fx, "y": fy})

    return {
        "grid_size": grid_size,
        "max_turns": 15,
        "current_turn": 1,
        "frog_a": {"x": 0, "y": 0, "goal": {"x": grid_size - 1, "y": grid_size - 1}, "score": 0},
        "frog_b": {"x": grid_size - 1, "y": grid_size - 1, "goal": {"x": 0, "y": 0}, "score": 0},
        "rocks": rocks,
        "flies": flies,
        "is_finished": False,
        "winner": None,
        "reason": "",
    }


def smart_2d_ai(frog_key: str, state_2d: dict) -> tuple[str, str]:
    """AI thong minh tim duong tranh da, san ruoi va chay ve dich."""
    me = state_2d[f"frog_{frog_key.lower()}"]
    opp_key = "b" if frog_key.lower() == "a" else "a"
    opp = state_2d[f"frog_{opp_key}"]

    rocks_set = {(r["x"], r["y"]) for r in state_2d["rocks"]}
    opp_pos = (opp["x"], opp["y"])
    curr_pos = (me["x"], me["y"])
    goal_pos = (me["goal"]["x"], me["goal"]["y"])
    flies_set = {(f["x"], f["y"]) for f in state_2d["flies"]}

    # Chon muc tieu: Ruoi gan nhat neu con duoi 3 buoc, nguoc lai la Dich
    target = goal_pos
    min_fly_dist = 999
    best_fly = None
    for fx, fy in flies_set:
        d = abs(curr_pos[0] - fx) + abs(curr_pos[1] - fy)
        if d < min_fly_dist:
            min_fly_dist = d
            best_fly = (fx, fy)

    if best_fly and min_fly_dist <= 3:
        target = best_fly
        thought = f"Phát hiện ruồi vàng gần ({target[0]},{target[1]}), lao tới ăn!"
    else:
        thought = f"Tiến về đích ({goal_pos[0]},{goal_pos[1]}) theo đường ngắn nhất!"

    # Tinh toan nuoc di hop le co khoang cach toi target nho nhat
    best_action = "wait"
    best_dist = 999

    for act, (dx, dy) in DELTAS_2D.items():
        if act == "wait":
            continue
        nx, ny = curr_pos[0] + dx, curr_pos[1] + dy
        if 0 <= nx < state_2d["grid_size"] and 0 <= ny < state_2d["grid_size"]:
            if (nx, ny) in rocks_set or (nx, ny) == opp_pos:
                continue
            dist = abs(nx - target[0]) + abs(ny - target[1])
            if dist < best_dist:
                best_dist = dist
                best_action = act

    return best_action, thought



class VuaCocHandler(BaseHTTPRequestHandler):
    """HTTP Request Handler xu ly static files va REST APIs cho VuaCoc Web."""

    def log_message(self, format, *args):
        # Giu console gon gang, chi in yeu cau chinh
        sys.stdout.write(f"[{self.log_date_time_string()}] {self.command} {self.path}\n")

    def send_json(self, data: dict | list, status: int = HTTPStatus.OK):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def send_error_json(self, message: str, status: int = HTTPStatus.BAD_REQUEST):
        self.send_json({"error": message, "success": False}, status=status)

    def do_OPTIONS(self):
        self.send_response(HTTPStatus.NO_CONTENT)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == "/api/bots":
            bots = [
                {"id": k, "name": v["name"], "description": v["desc"]}
                for k, v in BOT_REGISTRY.items()
            ]
            self.send_json({"bots": bots, "success": True})
            return

        if path == "/api/rules":
            rules = {
                "min_position": MIN_POSITION,
                "max_position": MAX_POSITION,
                "default_max_turns": DEFAULT_MAX_TURNS,
                "actions": ["left", "right", "wait"],
            }
            self.send_json({"rules": rules, "success": True})
            return

        # API: Tao game 2D moi
        if path == "/api/2d/new":
            new_game = create_2d_game()
            self.send_json({"success": True, "game": new_game})
            return

        # Serve static files
        if path == "/" or path == "":
            target_file = STATIC_DIR / "index.html"
        else:
            rel_path = path.lstrip("/")
            target_file = STATIC_DIR / rel_path

        if target_file.is_file() and target_file.resolve().is_relative_to(STATIC_DIR.resolve()):
            content_type, _ = mimetypes.guess_type(str(target_file))
            if not content_type:
                content_type = "application/octet-stream"
            content = target_file.read_bytes()
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", f"{content_type}; charset=utf-8" if "text" in content_type or "javascript" in content_type else content_type)
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        else:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.end_headers()

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path

        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length)

        try:
            body = json.loads(post_data.decode("utf-8")) if post_data else {}
        except json.JSONDecodeError:
            self.send_error_json("Dữ liệu gửi lên không phải JSON hợp lệ.")
            return

        # API 2D: Thuc hien 1 luot di trong ban co 2D
        if path == "/api/2d/step":
            game = body.get("game")
            if not game:
                self.send_error_json("Thiếu dữ liệu game 2D.")
                return

            action_a = body.get("action_a", "wait")
            mode = body.get("mode", "pve")  # "pve" (Human vs AI) hoac "pvp" (2 Players)
            action_b = body.get("action_b", "wait")
            thought_b = ""

            if mode == "pve":
                ai_action, thought_b = smart_2d_ai("b", game)
                action_b = ai_action

            rocks_set = {(r["x"], r["y"]) for r in game["rocks"]}
            grid_size = game["grid_size"]

            # Di chuyen Ech A
            dx_a, dy_a = DELTAS_2D.get(action_a, (0, 0))
            nx_a, ny_a = game["frog_a"]["x"] + dx_a, game["frog_a"]["y"] + dy_a
            if 0 <= nx_a < grid_size and 0 <= ny_a < grid_size and (nx_a, ny_a) not in rocks_set:
                game["frog_a"]["x"], game["frog_a"]["y"] = nx_a, ny_a

            # Di chuyen Ech B
            dx_b, dy_b = DELTAS_2D.get(action_b, (0, 0))
            nx_b, ny_b = game["frog_b"]["x"] + dx_b, game["frog_b"]["y"] + dy_b
            if 0 <= nx_b < grid_size and 0 <= ny_b < grid_size and (nx_b, ny_b) not in rocks_set:
                game["frog_b"]["x"], game["frog_b"]["y"] = nx_b, ny_b

            # Kiem tra an ruoi vang
            pos_a = (game["frog_a"]["x"], game["frog_a"]["y"])
            pos_b = (game["frog_b"]["x"], game["frog_b"]["y"])

            new_flies = []
            for f in game["flies"]:
                f_coord = (f["x"], f["y"])
                if f_coord == pos_a and f_coord == pos_b:
                    game["frog_a"]["score"] += 5
                    game["frog_b"]["score"] += 5
                elif f_coord == pos_a:
                    game["frog_a"]["score"] += 10
                elif f_coord == pos_b:
                    game["frog_b"]["score"] += 10
                else:
                    new_flies.append(f)
            game["flies"] = new_flies

            # Kiem tra cham dich
            reached_a = pos_a == (game["frog_a"]["goal"]["x"], game["frog_a"]["goal"]["y"])
            reached_b = pos_b == (game["frog_b"]["goal"]["x"], game["frog_b"]["goal"]["y"])

            if reached_a:
                game["frog_a"]["score"] += 50
            if reached_b:
                game["frog_b"]["score"] += 50

            if reached_a and reached_b:
                game["is_finished"] = True
                game["winner"] = "DRAW" if game["frog_a"]["score"] == game["frog_b"]["score"] else ("A" if game["frog_a"]["score"] > game["frog_b"]["score"] else "B")
                game["reason"] = "Cả 2 cùng chạm đích!"
            elif reached_a:
                game["is_finished"] = True
                game["winner"] = "A"
                game["reason"] = "Ếch A chạm đích trước!"
            elif reached_b:
                game["is_finished"] = True
                game["winner"] = "B"
                game["reason"] = "Ếch B chạm đích trước!"
            elif game["current_turn"] >= game["max_turns"]:
                game["is_finished"] = True
                score_a, score_b = game["frog_a"]["score"], game["frog_b"]["score"]
                game["winner"] = "DRAW" if score_a == score_b else ("A" if score_a > score_b else "B")
                game["reason"] = f"Hết lượt tối đa! Kết quả tính theo điểm số (A: {score_a}đ, B: {score_b}đ)."
            else:
                game["current_turn"] += 1

            turn_log = {
                "turn": game["current_turn"] - 1,
                "action_a": action_a,
                "action_b": action_b,
                "thought_b": thought_b,
                "pos_a": pos_a,
                "pos_b": pos_b,
                "score_a": game["frog_a"]["score"],
                "score_b": game["frog_b"]["score"],
            }

            self.send_json({
                "success": True,
                "game": game,
                "turn_log": turn_log,
            })
            return

        # API: Chạy 1 trận đấu trọn gói (Bot vs Bot 1D)
        if path == "/api/match":
            bot_a_key = body.get("bot_a", "forward")
            bot_b_key = body.get("bot_b", "cautious")
            max_turns = int(body.get("max_turns", DEFAULT_MAX_TURNS))
            custom_code = body.get("custom_code", "")

            # Xử lý Bot A
            if bot_a_key == "custom":
                bot_a_fn, err = create_custom_bot(custom_code)
                if err:
                    self.send_error_json(f"Bot A: {err}")
                    return
            else:
                bot_a_fn = BOT_REGISTRY.get(bot_a_key, {}).get("fn", forward_action)

            # Xử lý Bot B
            if bot_b_key == "custom":
                bot_b_fn, err = create_custom_bot(custom_code)
                if err:
                    self.send_error_json(f"Bot B: {err}")
                    return
            else:
                bot_b_fn = BOT_REGISTRY.get(bot_b_key, {}).get("fn", cautious_action)

            try:
                result = run_match(bot_a_fn, bot_b_fn, max_turns=max_turns)
                self.send_json({"success": True, "result": result.to_dict()})
            except Exception as e:
                self.send_error_json(f"Lỗi khi chạy trận đấu: {e}")
            return

        # API: Người chơi đi 1 bước trong chế độ Human vs Bot 1D
        if path == "/api/step":
            current_state = body.get("state", initial_state())
            turn = int(body.get("turn", 1))
            max_turns = int(body.get("max_turns", DEFAULT_MAX_TURNS))
            human_action = body.get("action", "wait")
            bot_b_key = body.get("opponent", "cautious")

            if human_action not in ("left", "right", "wait"):
                self.send_error_json(f"Hành động '{human_action}' không hợp lệ (chỉ chấp nhận left, right, wait).")
                return

            opponent_fn = BOT_REGISTRY.get(bot_b_key, {}).get("fn", cautious_action)

            # Bot B quan sát và chọn action
            view_b = bot_view(current_state, "B", turn, max_turns)
            try:
                bot_b_action = opponent_fn(view_b)
            except Exception:
                bot_b_action = "wait"

            # Áp dụng chuyển trạng thái
            new_pos_a = transition(current_state["bot_a_position"], human_action)
            new_pos_b = transition(current_state["bot_b_position"], bot_b_action)

            new_state = {
                "bot_a_position": new_pos_a,
                "bot_b_position": new_pos_b,
            }

            # Kiểm tra điều kiện thắng
            reached_a = new_pos_a == MAX_POSITION
            reached_b = new_pos_b == MIN_POSITION

            status = "in_progress"
            winner = None
            reason = ""

            if reached_a and reached_b:
                status = "completed"
                winner = None
                reason = "both_reached_goal"
            elif reached_a:
                status = "completed"
                winner = "A"
                reason = "bot_a_reached_goal"
            elif reached_b:
                status = "completed"
                winner = "B"
                reason = "bot_b_reached_goal"
            elif turn >= max_turns:
                status = "completed"
                winner = None
                reason = "max_turns_reached"

            step_record = {
                "turn_number": turn,
                "state_before": current_state,
                "bot_a_action": human_action,
                "bot_b_action": bot_b_action,
                "state_after": new_state,
            }

            self.send_json({
                "success": True,
                "turn_record": step_record,
                "new_state": new_state,
                "next_turn": turn + 1,
                "status": status,
                "winner": winner,
                "reason": reason,
            })
            return

        # API: Chạy Giải đấu Tournament toàn diện 1D
        if path == "/api/tournament":
            custom_code = body.get("custom_code", "")
            if custom_code.strip():
                bot_fn, err = create_custom_bot(custom_code)
                if err:
                    self.send_error_json(err)
                    return
                student_name = "Custom Bot (Bạn vừa viết)"
            else:
                bot_fn = student_action
                student_name = "Student Bot"

            opponents = {
                "forward": forward_action,
                "cautious": cautious_action,
                "wait": wait_action,
            }

            try:
                rows = evaluate_bot(bot_fn, opponents)
                summary = summarize_results(rows)
                self.send_json({
                    "success": True,
                    "student_name": student_name,
                    "standings": rows,
                    "summary": summary,
                })
            except Exception as e:
                self.send_error_json(f"Lỗi khi tổ chức giải đấu: {e}")
            return

        # API: Kiểm tra cú pháp và chạy thử Bot tùy chỉnh
        if path == "/api/test-bot":
            code = body.get("code", "")
            bot_fn, err = create_custom_bot(code)
            if err:
                self.send_error_json(err)
                return

            sample_state = {
                "turn": 1,
                "max_turns": 6,
                "position": 0,
                "opponent_position": 4,
                "goal": 4,
                "min_position": 0,
                "max_position": 4,
            }
            try:
                sample_action = bot_fn(sample_state)
                if sample_action not in ("left", "right", "wait"):
                    self.send_error_json(f"Bot trả về hành động không hợp lệ: '{sample_action}' (chỉ chấp nhận 'left', 'right', 'wait').")
                    return

                self.send_json({
                    "success": True,
                    "message": f"Mã nguồn hợp lệ! Với trạng thái mẫu, bot chọn: '{sample_action}'",
                    "sample_action": sample_action,
                })
            except Exception as e:
                self.send_error_json(f"Lỗi khi bot thực thi: {e}\n{traceback.format_exc()}")
            return

        self.send_response(HTTPStatus.NOT_FOUND)
        self.end_headers()


def start_server(port: int = 8080) -> None:
    STATIC_DIR.mkdir(parents=True, exist_ok=True)
    server_address = ("", port)
    httpd = ThreadingHTTPServer(server_address, VuaCocHandler)
    print("=" * 65)
    print("🐸  VUA CÓC BATTLE ARENA - WEB SERVER")
    print("=" * 65)
    print(f"[*] Máy chủ đang chạy tại: http://localhost:{port}")
    print("[*] Mở trình duyệt và truy cập đường link trên để trải nghiệm!")
    print("[*] Nhấn Ctrl+C để dừng máy chủ.")
    print("=" * 65)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Đang tắt máy chủ...")
        httpd.server_close()
        print("[+] Đã dừng máy chủ an toàn.")


if __name__ == "__main__":
    port_arg = 8080
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        port_arg = int(sys.argv[1])
    start_server(port_arg)
