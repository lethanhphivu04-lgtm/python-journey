"""
Bài tập 02: Các phương thức xử lý chuỗi (String Methods) 🛠️
=============================================================
Mục tiêu: Sử dụng strip, split, join, replace, upper, lower, find
"""

# TODO 1: Làm sạch và chuẩn hóa chuỗi người dùng nhập
raw = "   nguyen van an   "
cleaned = raw.strip().title()
print("Chuẩn hóa:", cleaned)
# -> Kết quả: Chuẩn hóa: Nguyen Van An

# TODO 2: Phân tích câu văn
sentence = "hello world python programming"
print("a)", sentence.title())
# -> Kết quả: Hello World Python Programming
print("b)", sentence.count("o"))
# -> Kết quả: 4
print("c)", sentence.replace("python", "PYTHON"))
# -> Kết quả: hello world PYTHON programming

# TODO 3: Nhập họ tên đầy đủ, tách ra họ và tên
ho_ten = input("Nhập họ tên đầy đủ: ").strip()
parts = ho_ten.split()
ho = parts[0] if parts else ""
ten = parts[-1] if len(parts) > 1 else ho
print(f"Họ: {ho}, Tên: {ten}")
# -> Kết quả mẫu ('Le Thanh Phi Vu'): Họ: Le, Tên: Vu

# TODO 4: Kiểm tra tên file hợp lệ
filename = input("Nhập tên file: ").strip().lower()
print("Hợp lệ:", filename.endswith((".py", ".txt", ".csv")))
# -> Kết quả mẫu ('test.py'): Hợp lệ: True

# TODO 5 (Thử thách): Mã hóa Caesar
text = input("Nhập chuỗi mã hóa Caesar: ")
shift = int(input("Số bước dịch (shift): "))

res = []
for c in text:
    if c.isalpha():
        base = ord("A") if c.isupper() else ord("a")
        res.append(chr((ord(c) - base + shift) % 26 + base))
    else:
        res.append(c)
print("Kết quả:", "".join(res))
# -> Kết quả mẫu ('abc', shift 3): Kết quả: def
