"""
Bài tập 02: Ép kiểu dữ liệu (Type Conversion) 🔄
==================================================
Mục tiêu: Chuyển đổi giữa int, float, str, bool
"""

# TODO 1: Chuyển đổi chuỗi thành số và cộng lại
s1 = "100"
s2 = "50"
total = int(s1) + int(s2)
print("Tổng:", total)
# -> Kết quả: Tổng: 150

# TODO 2: Chuyển float thành int và quan sát kết quả
pi = 3.99
print("int(pi):", int(pi))
# -> Kết quả: 3 (cắt bỏ phần thập phân, không làm tròn)

# TODO 3: Kiểm tra bool() của các giá trị
print(bool(0), bool(1), bool(""), bool("hello"), bool([]), bool([1, 2]))
# -> Kết quả: False True False True False True

# TODO 4: Nhập chiều cao (m) và cân nặng (kg) (kiểm tra đầu vào > 0 riêng từng mục)
while True:
    try:
        chieu_cao = float(input("Nhập chiều cao (m): "))
        if chieu_cao > 0:
            break
        print("Chiều cao phải lớn hơn 0, vui lòng nhập lại!")
    except ValueError:
        print("Vui lòng nhập số hợp lệ!")

while True:
    try:
        can_nang = float(input("Nhập cân nặng (kg): "))
        if can_nang > 0:
            break
        print("Cân nặng phải lớn hơn 0, vui lòng nhập lại!")
    except ValueError:
        print("Vui lòng nhập số hợp lệ!")

bmi = can_nang / (chieu_cao**2)
print(f"BMI: {bmi:.1f}")
# -> Kết quả mẫu (1.75m, 68kg): BMI: 22.2

# TODO 5 (Thử thách): Nhập số giây, chuyển sang giờ:phút:giây
while True:
    try:
        tong_giay = int(input("Nhập số giây (>=0): "))
        if tong_giay >= 0:
            break
        print("Số giây không được âm, vui lòng nhập lại!")
    except ValueError:
        print("Vui lòng nhập số nguyên!")

gio = tong_giay // 3600
phut = (tong_giay % 3600) // 60
giay = tong_giay % 60
print(f"{tong_giay} giây = {gio} giờ {phut} phút {giay} giây")
# -> Kết quả mẫu (3661s): 3661 giây = 1 giờ 1 phút 1 giây
