"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# TODO 1: ATM rút tiền
# Nhập số dư hiện tại và số tiền muốn rút
# Kiểm tra: số tiền rút > 0? Đủ số dư không? Bội số 50,000?
# In thông báo phù hợp
so_du = 1_000_000.0
tien_rut = float(input("Số tiền muốn rút: "))

if tien_rut <= 0:
    print("Số tiền rút phải lớn hơn 0")
elif tien_rut > so_du:
    print(f"Số dư không đủ (hiện có {so_du:,.0f} VNĐ)")
elif tien_rut % 50_000 != 0:
    print("Số tiền rút phải là bội số của 50,000 VNĐ")
else:
    so_du -= tien_rut
    print(f"Rút tiền thành công! Số dư còn lại: {so_du:,.0f} VNĐ")
# -> Kết quả mẫu (rút 200,000): Rút tiền thành công! Số dư còn lại: 800,000 VNĐ

# TODO 2: Xếp loại BMI
# Nhập chiều cao (m) và cân nặng (kg)
# BMI = weight / height^2
# < 18.5: Thiếu cân → gợi ý tăng cân
# 18.5-24.9: Bình thường → khen
# 25-29.9: Thừa cân → cảnh báo nhẹ
# >= 30: Béo phì → khuyến nghị gặp bác sĩ
h = float(input("Chiều cao (m): "))
w = float(input("Cân nặng (kg): "))

if h <= 0 or w <= 0:
    print("Chiều cao và cân nặng phải lớn hơn 0!")
else:
    bmi = w / (h**2)
    print(f"BMI: {bmi:.1f}")
    if bmi < 18.5:
        print("Thiếu cân - Nên bổ sung dinh dưỡng")
    elif bmi <= 24.9:
        print("Bình thường - Thể trạng tốt")
    elif bmi <= 29.9:
        print("Thừa cân - Cần vận động nhiều hơn")
    else:
        print("Béo phì - Khuyến nghị gặp bác sĩ")
# -> Kết quả mẫu (1.75m, 68kg):
# BMI: 22.2
# Bình thường - Thể trạng tốt

# TODO 3: Máy bán vé xem phim
# Nhập: loại vé (thuong/vip), ngày (thuong/cuoi_tuan), tuổi
# Giá cơ bản: thường 80k, VIP 120k
# Cuối tuần: +30%
# Trẻ em (<12) và người cao tuổi (>=65): giảm 50%
# Sinh viên (18-25): giảm 20%
# In giá vé cuối cùng
loai_ve = input("Loại vé (thuong/vip): ").strip().lower()
ngay = input("Ngày xem (thuong/cuoi_tuan): ").strip().lower()
tuoi = int(input("Tuổi: "))

gia = 120_000 if loai_ve == "vip" else 80_000
if ngay == "cuoi_tuan":
    gia *= 1.3

if tuoi < 12 or tuoi >= 65:
    gia *= 0.5
elif 18 <= tuoi <= 25:
    gia *= 0.8

print(f"Giá vé cuối cùng: {gia:,.0f} VNĐ")
# -> Kết quả mẫu (vip, cuoi_tuan, 20 tuổi): Giá vé cuối cùng: 124,800 VNĐ
