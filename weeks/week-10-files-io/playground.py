"""File thuc hanh tong hop Tuan 10 (Playground).
Test day du 3 the loai:
1. File TXT  (Nhat ky he thong - Server Log)
2. File CSV  (Bang diem hoc sinh - Students Table)
3. File JSON (Du lieu luu game RPG - Game Save)
"""

import csv
import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / ".learner-output"


# =====================================================================
# 1. THAO TAC VOI FILE TXT: Phan tich nhat ky Server Log
# =====================================================================
def xu_ly_file_txt() -> None:
    print("=" * 50)
    print("1. THAO TAC VOI FILE TXT (server_log.txt)")
    print("=" * 50)
    path = DATA_DIR / "server_log.txt"

    noi_dung = path.read_text(encoding="utf-8")
    cac_dong = noi_dung.splitlines()

    dem_info = 0
    dem_warning = 0
    dem_error = 0
    danh_sach_loi = []

    for dong in cac_dong:
        if "INFO:" in dong:
            dem_info += 1
        elif "WARNING:" in dong:
            dem_warning += 1
        elif "ERROR:" in dong:
            dem_error += 1
            danh_sach_loi.append(dong)

    print(f"Tong so dong log: {len(cac_dong)}")
    print(f"- So thong bao INFO: {dem_info}")
    print(f"- So canh bao WARNING: {dem_warning}")
    print(f"- So loi nguy hiem ERROR: {dem_error}")

    print("\nCac dong bi loi ERROR tim thay:")
    for loi in danh_sach_loi:
        print(f"  [!] {loi}")

    # TEST kiem thu xem co dung tim ra 2 loi khong
    assert dem_error == 2, f"Sai logic dem loi: {dem_error}"
    print("\n>> TEST TXT: PASS (Chinh xac 100%)!\n")


# =====================================================================
# 2. THAO TAC VOI FILE CSV: Tinh diem trung binh & Thu khoa
# =====================================================================
def xu_ly_file_csv() -> None:
    print("=" * 50)
    print("2. THAO TAC VOI FILE CSV (students.csv)")
    print("=" * 50)
    path = DATA_DIR / "students.csv"

    thu_khoa = ""
    diem_cao_nhat = 0.0

    print("Bang diem chi tiet:")
    with path.open(encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        for i, row in enumerate(reader, start=1):
            ten = row["name"]
            toan = float(row["math"])
            ly = float(row["physics"])
            anh = float(row["english"])

            dtb = round((toan + ly + anh) / 3, 2)
            print(f"{i}. {ten:8s} | Toan: {toan} | Ly: {ly} | Anh: {anh} => DTB: {dtb}")

            if dtb > diem_cao_nhat:
                diem_cao_nhat = dtb
                thu_khoa = ten

    print(f"\n==> THU KHOA: {thu_khoa} voi diem trung binh: {diem_cao_nhat}")

    # TEST kiem thu xem thu khoa co dung la Cuong khong
    assert thu_khoa == "Cuong", f"Thu khoa sai: {thu_khoa}"
    print(">> TEST CSV: PASS (Chinh xac 100%)!\n")


# =====================================================================
# 3. THAO TAC VOI FILE JSON: Doc, Nang cap trang bi va Ghi de
# =====================================================================
def xu_ly_file_json() -> None:
    print("=" * 50)
    print("3. THAO TAC VOI FILE JSON (game_save.json)")
    print("=" * 50)
    path = DATA_DIR / "game_save.json"

    # 1. Doc du lieu cu
    game_data = json.loads(path.read_text(encoding="utf-8"))
    print(f"Nhan vat: {game_data['player_name']} (Level {game_data['level']})")
    print(f"Vang hien co: {game_data['gold']}")
    print(f"So mon do trong tui: {len(game_data['inventory'])}")

    # 2. Xu ly du lieu trong bo nho (Nhat them do va tang vang)
    game_data["gold"] += 500  # Thuong 500 vang
    game_data["inventory"].append({
        "name": "Khien phep",
        "type": "shield",
        "power": 40
    })

    # 3. Ghi de file JSON moi xuong dia
    path.write_text(
        json.dumps(game_data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print("\n-> Da nhat them 'Khien phep' va cong 500 vang!")
    print(f"-> Vang moi: {game_data['gold']}")
    print(f"-> Tong so do trong tui sau khi nhat: {len(game_data['inventory'])}")

    # 4. Doc lai file de kiem thu xem da thuc su duoc ghi xuong dia chua
    reloaded = json.loads(path.read_text(encoding="utf-8"))
    assert len(reloaded["inventory"]) >= 4, "Loi chua ghi them do vao JSON!"
    print(">> TEST JSON: PASS (Chinh xac 100%)!\n")


# =====================================================================
# CHAY TOAN BO CAC DEMO
# =====================================================================
if __name__ == "__main__":
    xu_ly_file_txt()
    xu_ly_file_csv()
    xu_ly_file_json()
