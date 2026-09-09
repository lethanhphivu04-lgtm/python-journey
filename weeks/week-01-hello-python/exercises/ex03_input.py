"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào (kiểm tra không để trống)
while True:
    name = input("Bạn tên là gì? ").strip()
    if name:
        break
    print("Tên không được để trống, vui lòng nhập lại!")
print(f"Xin chào, {name}!")
# -> Kết quả: Xin chào, [name]!

# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh (kiểm tra phải là số)
while True:
    age_text = input("Bạn bao nhiêu tuổi? ").strip()
    if age_text.isdigit():
        age = int(age_text)
        break
    print("Tuổi phải là số nguyên, vui lòng nhập lại!")
print(f"Năm sinh ước tính: {2026 - age}")
# -> Kết quả: Năm sinh ước tính: [2026 - age]

# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
def nhap_so(prompt: str) -> float:
    while True:
        val = input(prompt).strip()
        try:
            return float(val)
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")

first = nhap_so("Nhập số thứ nhất: ")
second = nhap_so("Nhập số thứ hai: ")
print(f"Tổng: {first} + {second} = {first + second}")
# -> Kết quả: Tổng: [first] + [second] = [tổng]

# TODO 4 (Thử thách): Tạo Mad Libs mini (kiểm tra từng trường dữ liệu)
while True:
    n = input("Nhập tên: ").strip()
    if n:
        break
    print("Tên không được để trống, vui lòng nhập lại!")

while True:
    adj = input("Nhập tính từ: ").strip()
    if adj:
        break
    print("Tính từ không được để trống, vui lòng nhập lại!")

while True:
    pet = input("Nhập con vật: ").strip()
    if pet:
        break
    print("Con vật không được để trống, vui lòng nhập lại!")

while True:
    num = input("Nhập một số: ").strip()
    if num.isdigit():
        break
    print("Vui lòng nhập một số hợp lệ!")

print(f"{n} có một con {pet} rất {adj}. Mỗi ngày nó ăn {num} bát cơm!")
# -> Kết quả: [n] có một con [pet] rất [adj]. Mỗi ngày nó ăn [num] bát cơm!
