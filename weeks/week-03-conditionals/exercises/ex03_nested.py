"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# TODO 1: ATM rút tiền (lặp lại cho đến khi rút thành công)
so_du = 1_000_000.0
while True:
    try:
        tien_rut = float(input("Số tiền muốn rút: "))
        if tien_rut <= 0:
            print("Số tiền rút phải lớn hơn 0, vui lòng nhập lại!")
            continue
        if tien_rut > so_du:
            print(f"Số dư không đủ (hiện có {so_du:,.0f} VNĐ), vui lòng nhập lại!")
            continue
        if tien_rut % 50_000 != 0:
            print("Số tiền rút phải là bội số của 50,000 VNĐ, vui lòng nhập lại!")
            continue
        so_du -= tien_rut
        print(f"Rút tiền thành công! Số dư còn lại: {so_du:,.0f} VNĐ")
        break
    except ValueError:
        print("Vui lòng nhập số tiền hợp lệ!")
# -> Kết quả mẫu (rút 200,000): Rút tiền thành công! Số dư còn lại: 800,000 VNĐ

# TODO 2: Xếp loại BMI (nhập từng chỉ số với vòng lặp riêng)
while True:
    try:
        h = float(input("Chiều cao (m): "))
        if h > 0:
            break
        print("Chiều cao phải lớn hơn 0, vui lòng nhập lại!")
    except ValueError:
        print("Vui lòng nhập số hợp lệ!")

while True:
    try:
        w = float(input("Cân nặng (kg): "))
        if w > 0:
            break
        print("Cân nặng phải lớn hơn 0, vui lòng nhập lại!")
    except ValueError:
        print("Vui lòng nhập số hợp lệ!")

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
while True:
    loai_ve = input("Loại vé (thuong/vip): ").strip().lower()
    if loai_ve in ("thuong", "vip"):
        break
    print("Chỉ được nhập 'thuong' hoặc 'vip'!")

while True:
    ngay = input("Ngày xem (thuong/cuoi_tuan): ").strip().lower()
    if ngay in ("thuong", "cuoi_tuan"):
        break
    print("Chỉ được nhập 'thuong' hoặc 'cuoi_tuan'!")

while True:
    raw = input("Tuổi: ").strip()
    if raw.isdigit():
        tuoi = int(raw)
        break
    print("Vui lòng nhập số tuổi hợp lệ!")

gia = 120_000 if loai_ve == "vip" else 80_000
if ngay == "cuoi_tuan":
    gia *= 1.3

if tuoi < 12 or tuoi >= 65:
    gia *= 0.5
elif 18 <= tuoi <= 25:
    gia *= 0.8

print(f"Giá vé cuối cùng: {gia:,.0f} VNĐ")
# -> Kết quả mẫu (vip, cuoi_tuan, 20 tuổi): Giá vé cuối cùng: 124,800 VNĐ
