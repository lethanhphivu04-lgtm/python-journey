"""
Mini-Project: ASCII Art Generator 🎨
=====================================
Tạo chương trình in hình ASCII đẹp từ tên người dùng.
"""

# Bước 1: Hỏi tên người dùng (kiểm tra không rỗng)
ten = input("Nhập tên của bạn: ").strip()
while not ten:
    ten = input("Tên không được để trống, nhập lại: ").strip()

# Bước 2: Tính độ rộng khung
width = max(len(ten), 16) + 4
border = "═" * width

# Bước 3, 4, 5: In khung và nội dung
print(f"╔{border}╗")
print(f"║{'Xin chào'.center(width)}║")
print(f"║{ten.upper().center(width)}║")
print(f"║{'🐍 Python Journey 🐍'.center(width)}║")
print(f"╚{border}╝")
# -> Kết quả mẫu với tên 'Phi Vu':
# ╔════════════════════╗
# ║      Xin chào      ║
# ║       PHI VU       ║
# ║ 🐍 Python Journey 🐍 ║
# ╚════════════════════╝
