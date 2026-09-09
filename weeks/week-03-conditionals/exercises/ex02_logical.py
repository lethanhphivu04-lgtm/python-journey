"""
Bài tập 02: Toán tử logic 🧠
==============================
Mục tiêu: Kết hợp and, or, not trong điều kiện
"""

# TODO 1: Kiểm tra đủ điều kiện lái xe
while True:
    raw = input("Tuổi: ").strip()
    if raw.isdigit():
        tuoi = int(raw)
        break
    print("Tuổi phải là số nguyên, vui lòng nhập lại!")

while True:
    ans = input("Có bằng lái? (y/n): ").strip().lower()
    if ans in ("y", "n"):
        co_bang_lai = (ans == "y")
        break
    print("Vui lòng chỉ nhập 'y' hoặc 'n'!")

while True:
    ans = input("Tỉnh táo? (y/n): ").strip().lower()
    if ans in ("y", "n"):
        khong_say = (ans == "y")
        break
    print("Vui lòng chỉ nhập 'y' hoặc 'n'!")

if tuoi >= 18 and co_bang_lai and khong_say:
    print("Đủ điều kiện lái xe")
else:
    print("Không đủ điều kiện lái xe")
# -> Kết quả mẫu (20, y, y): Đủ điều kiện lái xe

# TODO 2: Phân loại tam giác
def nhap_canh(p: str) -> float:
    while True:
        try:
            val = float(input(p))
            if val > 0:
                return val
            print("Cạnh tam giác phải lớn hơn 0!")
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")

a = nhap_canh("Cạnh a: ")
b = nhap_canh("Cạnh b: ")
c = nhap_canh("Cạnh c: ")

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Tam giác đều")
    elif a == b or b == c or a == c:
        print("Tam giác cân")
    else:
        print("Tam giác thường")
else:
    print("Không phải tam giác")
# -> Kết quả mẫu (3, 4, 5): Tam giác thường

# TODO 3: Kiểm tra mật khẩu mạnh
while True:
    pw = input("Nhập mật khẩu: ").strip()
    if pw:
        break
    print("Mật khẩu không được để trống, vui lòng nhập lại!")

if (
    len(pw) >= 8
    and any(c.isupper() for c in pw)
    and any(c.islower() for c in pw)
    and any(c.isdigit() for c in pw)
):
    print("Mật khẩu mạnh")
else:
    print("Mật khẩu yếu")
# -> Kết quả mẫu ('MatKhau123'): Mật khẩu mạnh

# TODO 4 (Thử thách): FizzBuzz
while True:
    raw = input("Nhập số n: ").strip()
    if raw.lstrip("-").isdigit():
        n = int(raw)
        break
    print("Vui lòng nhập số nguyên!")

if n % 15 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
# -> Kết quả mẫu (15): FizzBuzz
