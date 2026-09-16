"""
Bài tập 01: if/elif/else cơ bản 🔀
====================================
Mục tiêu: Viết câu lệnh điều kiện đúng cú pháp
"""

# TODO 1: Nhập tuổi, in ra nhóm tuổi
tuoi = int(input("Nhập tuổi: "))
if tuoi < 13:
    print("Thiếu nhi")
elif tuoi <= 17:
    print("Thiếu niên")
elif tuoi <= 64:
    print("Người lớn")
else:
    print("Người cao tuổi")
# -> Kết quả mẫu (20): Người lớn

# TODO 2: Nhập điểm (0-10), xếp loại
diem = float(input("Nhập điểm (0-10): "))
if diem < 0 or diem > 10:
    print("Điểm không hợp lệ")
elif diem >= 9:
    print("Xuất sắc")
elif diem >= 8:
    print("Giỏi")
elif diem >= 6.5:
    print("Khá")
elif diem >= 5:
    print("TB")
else:
    print("Yếu")
# -> Kết quả mẫu (8.5): Giỏi

# TODO 3: Nhập năm, kiểm tra năm nhuận
nam = int(input("Nhập năm: "))
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print("Năm nhuận")
else:
    print("Không phải năm nhuận")
# -> Kết quả mẫu (2024): Năm nhuận

# TODO 4 (Thử thách): Nhập 3 số, in ra số lớn nhất
# Không dùng hàm max(), chỉ dùng if/elif/else
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
if a >= b and a >= c:
    so_lon_nhat = a
elif b >= a and b >= c:
    so_lon_nhat = b
else:
    so_lon_nhat = c
print("Số lớn nhất:", so_lon_nhat)
# -> Kết quả mẫu (5, 12, 9): Số lớn nhất: 12.0
