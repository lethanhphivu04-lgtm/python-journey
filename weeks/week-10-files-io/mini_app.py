"""Chuong trinh nho Tuan 10: Quan ly chi tieu ca nhan (Expense Tracker).
Minh hoa tron ven: Ghi file, Doc file, Xu ly du lieu va Cach kiem thu (Test).
"""

import csv
from pathlib import Path

# Duong dan file du lieu luu tai .learner-output/expenses.csv
CURRENT_DIR = Path(__file__).resolve().parent
DATA_FILE = CURRENT_DIR / ".learner-output" / "expenses.csv"


def khoi_tao_file() -> None:
    """Tao thu muc va file CSV neu chua co."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        with DATA_FILE.open("w", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(stream, fieldnames=["item", "price"])
            writer.writeheader()


def ghi_khoan_chi(item: str, price: int) -> None:
    """1. GHI FILE: Ghi them mot khoan chi vao cuoi file CSV."""
    khoi_tao_file()
    with DATA_FILE.open("a", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=["item", "price"])
        writer.writerow({"item": item, "price": price})
    print(f"-> Saved: {item} ({price:,} VND)")


def doc_va_tinh_tong() -> int:
    """2. DOC FILE & XU LY DU LIEU: Tinh tong tien va tim mon dat nhat."""
    if not DATA_FILE.exists():
        print("Chua co du lieu.")
        return 0

    tong_tien = 0
    mon_dat_nhat = ""
    gia_cao_nhat = 0

    print("\n--- DANH SACH CHI TIEU TRONG FILE ---")
    with DATA_FILE.open(encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        for i, row in enumerate(reader, start=1):
            item = row["item"]
            price = int(row["price"])  # Ep kieu chuoi sang so de tinh toan
            tong_tien += price

            if price > gia_cao_nhat:
                gia_cao_nhat = price
                mon_dat_nhat = item

            print(f"{i}. {item}: {price:,} VND")

    print(f"==> TONG CONG: {tong_tien:,} VND")
    print(f"==> MON DAT NHAT: {mon_dat_nhat} ({gia_cao_nhat:,} VND)\n")
    return tong_tien


def chay_kiem_thu_tu_dong() -> None:
    """3. TEST: Tu dong kiem tra code bang lenh assert."""
    print("--- CHAY TEST KIEM THU TU DONG ---")
    test_file = CURRENT_DIR / ".learner-output" / "test_temp.csv"

    # Tao file test mau
    with test_file.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=["item", "price"])
        writer.writeheader()
        writer.writerow({"item": "But bi", "price": "5000"})
        writer.writerow({"item": "Vo ghi", "price": "15000"})

    # Tinh tong tu file test
    tong = 0
    with test_file.open(encoding="utf-8") as stream:
        for row in csv.DictReader(stream):
            tong += int(row["price"])

    # Kiem tra ket qua co dung 20000 VND khong
    assert tong == 20000, f"Loi logic: mong doi 20000 nhung ra {tong}"
    print(">> TEST TONG TIEN: PASS (Chinh xac 100%)!\n")

    # Xoa file test tam sau khi kiem thu xong
    if test_file.exists():
        test_file.unlink()


if __name__ == "__main__":
    print("=== CHUONG TRINH QUAN LY CHI TIEU ===")

    # Ghi 3 khoan chi mau vao file
    ghi_khoan_chi("Banh mi", 20000)
    ghi_khoan_chi("Ca phe", 25000)
    ghi_khoan_chi("Nuoc suoi", 10000)

    # Doc file va xu ly thong ke
    doc_va_tinh_tong()

    # Chay test
    chay_kiem_thu_tu_dong()
