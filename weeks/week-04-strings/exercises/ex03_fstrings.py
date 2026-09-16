"""
Bài tập 03: f-string formatting 💅
====================================
Mục tiêu: Định dạng output đẹp với f-string
"""

# TODO 1: Cho ten = "An", tuoi = 20, diem = 8.567
ten = "An"
tuoi = 20
diem = 8.567
print(f"Học sinh {ten}, {tuoi} tuổi, điểm TB: {diem:.2f}")
# -> Kết quả: Học sinh An, 20 tuổi, điểm TB: 8.57

# TODO 2: In bảng cửu chương 5 với cột thẳng hàng
for i in range(1, 11):
    print(f"5 x {i:>2} = {5 * i:>3}")
# -> Kết quả:
# 5 x  1 =   5
# 5 x  2 =  10
# ...
# 5 x 10 =  50

# TODO 3: In hóa đơn mua hàng đẹp
print("===========================")
print(f"{'SẢN PHẨM':<15}{'GIÁ (VNĐ)':>12}")
print("---------------------------")
print(f"{'Cà phê':<15}{35_000:>12,}")
print(f"{'Bánh mì':<15}{25_000:>12,}")
print(f"{'Nước suối':<15}{10_000:>12,}")
print("---------------------------")
print(f"{'TỔNG CỘNG':<15}{70_000:>12,}")
print("===========================")
# -> Kết quả: Các cột chữ và số được căn lề thẳng tắp

# TODO 4 (Thử thách): Tạo progress bar bằng f-string
pct = int(input("Nhập phần trăm (0-100): "))
filled = pct // 5
empty = 20 - filled
print(f"[{'█' * filled}{'░' * empty}] {pct}%")
# -> Kết quả mẫu (40%): [████████░░░░░░░░░░░░] 40%
