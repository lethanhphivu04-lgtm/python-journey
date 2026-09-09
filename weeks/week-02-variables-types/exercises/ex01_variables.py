"""
Bài tập 01: Biến trong Python 📦
=================================
Mục tiêu: Hiểu cách khai báo và sử dụng biến
"""

# TODO 1: Tạo 4 biến lưu thông tin cá nhân
ten = "Lê Thanh Phi Vũ"
tuoi = 20
diem_tb = 8.5
dang_hoc = True
print(f"ten: {ten} ({type(ten)})")
print(f"tuoi: {tuoi} ({type(tuoi)})")
print(f"diem_tb: {diem_tb} ({type(diem_tb)})")
print(f"dang_hoc: {dang_hoc} ({type(dang_hoc)})")
# -> Kết quả:
# ten: Lê Thanh Phi Vũ (<class 'str'>)
# tuoi: 20 (<class 'int'>)
# diem_tb: 8.5 (<class 'float'>)
# dang_hoc: True (<class 'bool'>)

# TODO 2: Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm
a = 10
b = 20
a, b = b, a
print(f"a = {a}, b = {b}")
# -> Kết quả: a = 20, b = 10

# TODO 3: Augmented assignment
x = 100
x += 50
print("Sau +=", x)  # -> Kết quả: 150
x -= 20
print("Sau -=", x)  # -> Kết quả: 130
x *= 2
print("Sau *=", x)  # -> Kết quả: 260
x //= 4
print("Sau //=", x) # -> Kết quả: 65

# TODO 4 (Thử thách): Multiple assignment
ho, ten, tuoi = "Lê Thanh", "Phi Vũ", 20
print(f"Họ tên: {ho} {ten}, {tuoi} tuổi")
# -> Kết quả: Họ tên: Lê Thanh Phi Vũ, 20 tuổi
