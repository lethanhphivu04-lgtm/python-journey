"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

def nhap_float(prompt: str, duong: bool = False) -> float:
    while True:
        try:
            val = float(input(prompt))
            if duong and val <= 0:
                print("Giá trị phải lớn hơn 0!")
                continue
            return val
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
a = nhap_float("Nhập số thứ nhất: ")
while True:
    b = nhap_float("Nhập số thứ hai: ")
    if b != 0:
        break
    print("Số thứ hai phải khác 0 để thực hiện phép chia!")

print(f"Tổng: {a + b}, Hiệu: {a - b}, Tích: {a * b}, Thương: {a / b}")
# -> Kết quả mẫu (10, 5): Tổng: 15.0, Hiệu: 5.0, Tích: 50.0, Thương: 2.0

# TODO 2: Nhập bán kính hình tròn, tính và in chu vi & diện tích
r = nhap_float("Nhập bán kính r: ", duong=True)
pi = 3.14159
print(f"Diện tích: {pi * r**2:.2f}, Chu vi: {2 * pi * r:.2f}")
# -> Kết quả mẫu (r=7): Diện tích: 153.94, Chu vi: 43.98

# TODO 3: Nhập giá gốc và % giảm giá
gia_goc = nhap_float("Nhập giá gốc: ", duong=True)
giam_gia = nhap_float("Nhập % giảm giá (0-100): ")
gia_sau_giam = gia_goc * (1 - giam_gia / 100)
print(f"Giá sau giảm: {gia_sau_giam:,.0f} VNĐ")
# -> Kết quả mẫu (500000, 20%): Giá sau giảm: 400,000 VNĐ

# TODO 4 (Thử thách): Máy đổi tiền
vnd = nhap_float("Nhập số tiền VNĐ: ", duong=True)
ty_gia = nhap_float("Nhập tỷ giá USD/VNĐ: ", duong=True)
print(f"Số USD: {vnd / ty_gia:.2f} USD")
# -> Kết quả mẫu (250000 VNĐ, tỷ giá 25000): Số USD: 10.00 USD
