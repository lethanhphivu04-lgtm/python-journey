"""
Bài tập 01: Indexing & Slicing chuỗi 🔤
=========================================
Mục tiêu: Thành thạo truy cập và cắt chuỗi
"""

# TODO 1: Cho s = "Python Journey"
s = "Python Journey"
print("Ký tự đầu:", s[0])        # -> 'P'
print("Ký tự cuối:", s[-1])      # -> 'y'
print("5 ký tự đầu:", s[:5])     # -> 'Pytho'

# TODO 2: Dùng slicing
print("a)", s[7:])               # -> 'Journey'
print("b)", s[::-1])             # -> 'yenruoJ nohtyP'
print("c)", s[::2])              # -> 'Pto ore'

# TODO 3: Nhập CCCD (12 chữ số)
cccd = input("Nhập CCCD (12 chữ số): ").strip()
print(f"Mã tỉnh: {cccd[:3]}, Giới tính: {cccd[3]}, Năm sinh: {cccd[4:6]}")
# -> Kết quả mẫu ('079099012345'): Mã tỉnh: 079, Giới tính: 0, Năm sinh: 99

# TODO 4 (Thử thách): Kiểm tra chuỗi đối xứng (palindrome)
text = input("Nhập chuỗi kiểm tra palindrome: ").strip()
clean = "".join(text.lower().split())
print("Đối xứng:", clean == clean[::-1])
# -> Kết quả mẫu ('racecar'): Đối xứng: True
