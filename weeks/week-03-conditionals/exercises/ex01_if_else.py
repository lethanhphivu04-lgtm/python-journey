"""
Bài tập 01: if/elif/else cơ bản 🔀
====================================
Mục tiêu: Viết câu lệnh điều kiện đúng cú pháp
"""

# TODO 1: Nhập tuổi, in ra nhóm tuổi
while True:
    raw = input("Nhập tuổi: ").strip()
    if raw.isdigit():
        tuoi = int(raw)
        break
    print("Vui lòng nhập số tuổi hợp lệ!")

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
while True:
    try:
        diem = float(input("Nhập điểm (0-10): "))
        if 0 <= diem <= 10:
            break
        print("Điểm phải nằm trong thang 0 đến 10!")
    except ValueError:
        print("Vui lòng nhập điểm dạng số!")

if diem >= 9:
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
while True:
    raw = input("Nhập năm: ").strip()
    if raw.isdigit():
        nam = int(raw)
        break
    print("Vui lòng nhập năm dạng số nguyên!")

if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print("Năm nhuận")
else:
    print("Không phải năm nhuận")
# -> Kết quả mẫu (2024): Năm nhuận

# TODO 4 (Thử thách): Nhập 3 số, in ra số lớn nhất
def nhap_float(p: str) -> float:
    while True:
        try:
            return float(input(p))
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")

a = nhap_float("Nhập số thứ nhất: ")
b = nhap_float("Nhập số thứ hai: ")
c = nhap_float("Nhập số thứ ba: ")
if a >= b and a >= c:
    so_lon_nhat = a
elif b >= a and b >= c:
    so_lon_nhat = b
else:
    so_lon_nhat = c
print("Số lớn nhất:", so_lon_nhat)
# -> Kết quả mẫu (5, 12, 9): Số lớn nhất: 12.0
