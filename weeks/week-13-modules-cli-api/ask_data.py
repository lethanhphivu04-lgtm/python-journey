"""Tro ly hoi dap du lieu thong minh (Interactive Data Q&A Assistant).
Cho phep nguoi dung dat cau hoi bang tieng Viet ve file du lieu va nhan cau tra loi ngay lap tuc!
Khong can API key, chay 100% offline, hieu ca tieng Viet co dau va khong dau.
"""

import csv
import json
import sys
import unicodedata
from pathlib import Path
from urllib.request import Request, urlopen

# Dam bao terminal Windows in tieng Viet dep
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parents[2]
STUDENTS_FILE = ROOT_DIR / "weeks" / "week-10-files-io" / ".learner-output" / "students.csv"
EXPENSES_FILE = ROOT_DIR / "weeks" / "week-10-files-io" / ".learner-output" / "expenses.csv"


def bo_dau(text: str) -> str:
    """Chuyen chu co dau thanh khong dau de so sanh de dang (vi du: 'Toán' -> 'toan')."""
    text = unicodedata.normalize("NFD", text)
    text = "".join(ch for ch in text if unicodedata.category(ch) != "Mn")
    return text.lower().strip()


def doc_hoc_sinh() -> list[dict]:
    if not STUDENTS_FILE.exists():
        return []
    with STUDENTS_FILE.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def doc_chi_tieu() -> list[dict]:
    if not EXPENSES_FILE.exists():
        return []
    with EXPENSES_FILE.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def tra_loi_cau_hoi(cau_hoi: str) -> str:
    q = bo_dau(cau_hoi)
    hoc_sinh = doc_hoc_sinh()
    chi_tieu = doc_chi_tieu()

    # 1. Hoi ve hoc sinh / diem so
    if any(k in q for k in ["thu khoa", "cao nhat", "gioi nhat", "top 1"]):
        if not hoc_sinh:
            return "Chua co du lieu hoc sinh."
        top_hs = max(hoc_sinh, key=lambda x: (float(x["math"]) + float(x["physics"]) + float(x["english"])) / 3)
        dtb = round((float(top_hs["math"]) + float(top_hs["physics"]) + float(top_hs["english"])) / 3, 2)
        return f"🏆 Thu khoa la ban {top_hs['name']} voi DTB: {dtb} (Toan: {top_hs['math']}, Ly: {top_hs['physics']}, Anh: {top_hs['english']})!"

    if any(k in q for k in ["thap nhat", "yeu nhat", "kem nhat"]):
        if not hoc_sinh:
            return "Chua co du lieu hoc sinh."
        bot_hs = min(hoc_sinh, key=lambda x: (float(x["math"]) + float(x["physics"]) + float(x["english"])) / 3)
        dtb = round((float(bot_hs["math"]) + float(bot_hs["physics"]) + float(bot_hs["english"])) / 3, 2)
        return f"Ban co diem thap nhat la {bot_hs['name']} voi DTB: {dtb}."

    if any(k in q for k in ["bao nhieu hoc sinh", "si so", "tong so hoc sinh"]):
        return f"Hien co tong cong {len(hoc_sinh)} hoc sinh trong danh sach."

    if any(k in q for k in ["trung binh ca lop", "dtb ca lop"]):
        if not hoc_sinh:
            return "Chua co du lieu."
        tong = sum((float(x["math"]) + float(x["physics"]) + float(x["english"])) / 3 for x in hoc_sinh)
        return f"Diem trung binh chung cua ca lop la: {round(tong / len(hoc_sinh), 2)} diem."

    # Kiem tra hoi diem cua mot ban cu the (An, Binh, Cuong, Dung, Hoa)
    for hs in hoc_sinh:
        ten_hs = bo_dau(hs["name"])
        if ten_hs in q:
            dtb = round((float(hs["math"]) + float(hs["physics"]) + float(hs["english"])) / 3, 2)
            return (
                f"📊 Thong tin ban {hs['name']}:\n"
                f"   - Toan: {hs['math']} | Ly: {hs['physics']} | Anh: {hs['english']}\n"
                f"   - Diem trung binh: {dtb}"
            )

    # 2. Hoi ve chi tieu (expenses)
    if any(k in q for k in ["tong chi tieu", "tong tien", "da tieu bao nhieu", "het bao nhieu"]):
        if not chi_tieu:
            return "Chua co du lieu chi tieu."
        tong = sum(int(x["price"]) for x in chi_tieu)
        return f"💰 Tong so tien ban da chi tieu la: {tong:,} VND."

    if any(k in q for k in ["dat nhat", "ton nhat", "gia cao nhat"]):
        if not chi_tieu:
            return "Chua co du lieu chi tieu."
        mon_top = max(chi_tieu, key=lambda x: int(x["price"]))
        return f"Món chi dat nhat la '{mon_top['item']}' voi gia {int(mon_top['price']):,} VND."

    # 3. Hoi ve GitHub cua ban
    if any(k in q for k in ["github", "tj", "repo", "tai khoan"]):
        try:
            req = Request("https://api.github.com/users/lethanhphivu04-lgtm", headers={"User-Agent": "Python"})
            with urlopen(req, timeout=5) as resp:
                gh = json.loads(resp.read().decode("utf-8"))
                return (
                    f"🐙 Thong tin GitHub cua ban ({gh['login']}):\n"
                    f"   - Ten: {gh.get('name')}\n"
                    f"   - So Repositories cong khai: {gh.get('public_repos')}\n"
                    f"   - Noi o: {gh.get('location')}\n"
                    f"   - Bio: {gh.get('bio', '').strip()}"
                )
        except Exception:
            return "Khong the ket noi den GitHub API luc nay."

    # 4. Xem toan bo danh sach
    if any(k in q for k in ["danh sach", "xem het", "tat ca"]):
        ket_qua = ["Danh sach tat ca hoc sinh:"]
        for hs in hoc_sinh:
            dtb = round((float(hs["math"]) + float(hs["physics"]) + float(hs["english"])) / 3, 2)
            ket_qua.append(f"- {hs['name']:8s} | DTB: {dtb}")
        return "\n".join(ket_qua)

    return (
        "Xin loi, toi chua hieu cau hoi cua ban. Ban co the hoi:\n"
        "- 'Ai diem cao nhat?' hoac 'Thu khoa la ai?'\n"
        "- 'Diem cua Cuong' hoac 'Diem cua An the nao?'\n"
        "- 'Tong chi tieu la bao nhieu?'\n"
        "- 'Mon nao dat nhat?'\n"
        "- 'Thong tin github cua toi?'"
    )


def chay_interactive() -> None:
    print("=" * 65)
    print("🤖 CHAO MUNG BAN DEN VOI TRO LY HOI DAP DU LIEU PYTHON!")
    print("   Ban co the hoi bat ky dieu gi ve diem so, chi tieu, hoac GitHub.")
    print("   (Go 'thoat' hoac 'exit' de dung chuong trinh)")
    print("=" * 65)

    while True:
        try:
            cau_hoi = input("\n👉 BAN HOI: ").strip()
            if not cau_hoi:
                continue

            if bo_dau(cau_hoi) in ["thoat", "exit", "quit", "dung"]:
                print("👋 Tam biet ban! Hen gap lai.")
                break

            tra_loi = tra_loi_cau_hoi(cau_hoi)
            print(f"💡 TRO LY:\n{tra_loi}")

        except (KeyboardInterrupt, EOFError):
            print("\n👋 Tam biet ban!")
            break


if __name__ == "__main__":
    chay_interactive()
