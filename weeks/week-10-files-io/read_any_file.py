"""Doc va hien thi bat ky file CSV nao tu ben ngoai truyen vao.
Cach chay: python weeks/week-10-files-io/read_any_file.py <duong_dan_file_csv>
"""

import csv
import sys
from pathlib import Path


def doc_va_hien_thi_csv(file_path_str: str) -> None:
    path = Path(file_path_str).resolve()
    print("=" * 65)
    print(f"[*] DANG DOC FILE CSV: {path.name}")
    print(f"[*] DUONG DAN: {path}")
    print("=" * 65)

    if not path.exists():
        print(f"[!] LOI: Khong tim thay file tai dia chi tren!")
        print(f"    Goi y: Hay kiem tra lai xem duong dan co go dung chua nhe.")
        return

    size_bytes = path.stat().st_size
    print(f"[+] Kich thuoc: {size_bytes} bytes")

    with path.open(encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        fieldnames = reader.fieldnames

        if not fieldnames:
            print("[!] File CSV rong (khong co cot nao).")
            return

        print(f"[+] Cac cot trong file: {', '.join(fieldnames)}")
        print("\n--- NOI DUNG CHI TIET TUNG HANG ---")

        hang_so = 0
        for i, row in enumerate(reader, start=1):
            hang_so = i
            # In cac cot dep mat
            dong_in = " | ".join(f"{col}: {val}" for col, val in row.items())
            print(f"Hang {i:2d}: {dong_in}")

        print("=" * 65)
        print(f"-> TONG CONG: Da doc thanh cong {hang_so} hang du lieu!")
        print("=" * 65)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_path = sys.argv[1]
    else:
        target_path = "weeks/week-10-files-io/.learner-output/students.csv"

    doc_va_hien_thi_csv(target_path)
