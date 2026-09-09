"""Starter for the Week 02 student card."""

while True:
    name = input("Họ tên: ").strip()
    if name:
        break
    print("Họ tên không được rỗng, vui lòng nhập lại!")

while True:
    student_id = input("Mã sinh viên: ").strip()
    if student_id:
        break
    print("Mã sinh viên không được rỗng, vui lòng nhập lại!")

while True:
    major = input("Ngành: ").strip()
    if major:
        break
    print("Ngành không được rỗng, vui lòng nhập lại!")

while True:
    start_year_text = input("Năm nhập học: ").strip()
    if start_year_text.isdigit() and len(start_year_text) == 4:
        break
    print("Năm nhập học cần là số có 4 chữ số (ví dụ 2023), vui lòng nhập lại!")

start_year = int(start_year_text)
graduation_year = start_year + 4
print(f"{name} · {student_id} · {major}")
print(f"Khóa: {start_year}–{graduation_year}")
# -> Kết quả mẫu:
# Le Thanh Phi Vu · 2123110178 · Cong nghe thong tin
# Khóa: 2023–2027
