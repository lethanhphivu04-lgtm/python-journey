"""Tro ly AI hoi dap du lieu thong minh su dung Google Gemini API.
Hoat dong 100% bang thu vien chuan urllib va json (khong can cai dat them gi).
Tu dong doc du lieu tu students.csv, expenses.csv, game_save.json de tra loi bat ky cau hoi nao.
"""

import json
import os
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

# Dam bao in tieng Viet UTF-8 dep tren moi terminal Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parents[2]


def doc_api_key() -> str:
    """Lay API key tu file .env hoac bien moi truong."""
    env_file = ROOT_DIR / ".env"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("GEMINI_API_KEY="):
                return line.split("=", 1)[1].strip()
    return os.environ.get("GEMINI_API_KEY", "")


def thu_thap_du_lieu_he_thong() -> str:
    """Doc tat ca file du lieu trong project de dua lam ngu canh cho AI."""
    output_dir = ROOT_DIR / "weeks" / "week-10-files-io" / ".learner-output"
    ngu_canh = []

    # 1. Bang diem students.csv
    students_file = output_dir / "students.csv"
    if students_file.exists():
        ngu_canh.append(f"--- DU LIEU HOC SINH (students.csv) ---\n{students_file.read_text(encoding='utf-8')}")

    # 2. Chi tieu expenses.csv
    expenses_file = output_dir / "expenses.csv"
    if expenses_file.exists():
        ngu_canh.append(f"--- DU LIEU CHI TIEU (expenses.csv) ---\n{expenses_file.read_text(encoding='utf-8')}")

    # 3. Game save json
    game_file = output_dir / "game_save.json"
    if game_file.exists():
        ngu_canh.append(f"--- DU LIEU GAME SAVE (game_save.json) ---\n{game_file.read_text(encoding='utf-8')}")

    # 4. Thong tin GitHub chu nhan
    ngu_canh.append(
        "--- THONG TIN NGUOI DUNG GITHUB ---\n"
        "Username: lethanhphivu04-lgtm\n"
        "Ten: TJ\n"
        "Truong: Cao Dang Cong Thuong TP.HCM\n"
        "Vi tri: Ho Chi Minh\n"
        "Public Repos: 13"
    )

    return "\n\n".join(ngu_canh)


def hoi_gemini_ai(api_key: str, cau_hoi: str, du_lieu_context: str) -> str:
    """Gui cau hoi kem du lieu toi Google Gemini 3.8 Flash de lay cau tra loi thong minh."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={api_key}"

    prompt = (
        "Ban la tro ly AI thong minh chuyen phan tich du lieu cho hoc vien Python Journey.\n"
        "Duoi day la toan bo cac file du lieu hien co cua he thong:\n"
        f"{du_lieu_context}\n\n"
        f"Hay tra loi cau hoi sau cua nguoi dung dua tren cac du lieu tren bang tieng Viet tu nhien, "
        f"chinh xac, than thien va ro rang:\n"
        f"Cau hoi: {cau_hoi}"
    )

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    req = Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    try:
        with urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data["candidates"][0]["content"]["parts"][0]["text"].strip()
    except HTTPError as e:
        error_msg = e.read().decode("utf-8")
        return f"[!] Loi HTTP ({e.code}): {error_msg}"
    except URLError as e:
        return f"[!] Loi ket noi mang: {e.reason}"
    except Exception as e:
        return f"[!] Loi: {e}"


def chay_tro_ly_ai() -> None:
    api_key = doc_api_key()
    if not api_key:
        print("[!] Khong tim thay GEMINI_API_KEY trong file .env!")
        return

    print("=" * 65)
    print("🤖 TRO LY AI THONG MINH PHAN TICH DU LIEU (GOOGLE GEMINI 3.8)")
    print("   Da ket noi thanh cong voi API Key cua ban.")
    print("   AI da doc toan bo du lieu: students.csv, expenses.csv, game_save.json.")
    print("   Ban co the hoi BAT KY dieu gi bang tieng Viet tu nhien!")
    print("   (Go 'thoat' hoac 'exit' de dung)")
    print("=" * 65)

    du_lieu = thu_thap_du_lieu_he_thong()

    while True:
        try:
            cau_hoi = input("\n👉 BAN HOI: ").strip()
            if not cau_hoi:
                continue

            if cau_hoi.lower() in ["thoat", "exit", "quit", "dung"]:
                print("👋 Tam biet ban!")
                break

            print("⏳ AI dang suy nghi va phan tich...")
            tra_loi = hoi_gemini_ai(api_key, cau_hoi, du_lieu)
            print(f"\n💡 AI TRA LOI:\n{tra_loi}\n")
            print("-" * 65)

        except (KeyboardInterrupt, EOFError):
            print("\n👋 Tam biet ban!")
            break


if __name__ == "__main__":
    chay_tro_ly_ai()
