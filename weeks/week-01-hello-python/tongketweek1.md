# Tổng kết kiến thức Tuần 01: Môi trường, lệnh print, số học và input

- Sinh viên: Lê Thanh Phi Vũ
- MSSV: 2123110178
- Môn học: Lập trình Python

---

## 1. Những khái niệm cốt lõi cần nhớ

- Quy trình cơ bản của một chương trình: Người dùng nhập dữ liệu vào (input) -> Python tính toán, xử lý -> Xuất kết quả ra màn hình (print).
- Cách chạy file code trong terminal: `python ten_file.py`
- Dữ liệu nhận từ hàm `input()` luôn luôn là dạng chữ (string). Muốn dùng nó để cộng, trừ, nhân, chia thì bắt buộc phải đổi sang kiểu số (`int` hoặc `float`).

---

## 2. Giải thích chi tiết code và giải thuật từng bài

### Bài 1: Lệnh in ra màn hình (ex01_hello.py)

Mục đích bài này là làm quen với hàm `print()`.

Code:
```python
print("Hello, World!")
print("Lê Thanh Phi Vũ")
print("Thích xem phim\nThích lập trình Python\nThích chơi game")
print("*****\n*   *\n*   *\n*****")
print("V     V  U   U\n V   V   U   U\n  V V    U   U\n   V      UUU")
```

Giải thích:
- `print(...)` dùng để in dữ liệu trong ngoặc ra màn hình terminal.
- Ký tự `\n` đại diện cho việc bấm phím Enter xuống dòng. Thay vì phải viết 3 lần hàm `print()`, ta chỉ cần viết 1 dòng và chèn `\n` vào giữa các câu để ngắt dòng. Tiết kiệm code và chạy nhanh hơn.
- Hình chữ nhật và chữ nghệ thuật: terminal hiển thị các ký tự với độ rộng bằng nhau (font monospace), nên chỉ cần căn chỉnh số dấu cách và dấu `*` tương ứng là hình sẽ thẳng hàng.

---

### Bài 2: Các phép tính số học (ex02_calculator.py)

Mục đích bài này là dùng Python như một chiếc máy tính bỏ túi.

Code:
```python
print(2024 + 1000)
print(150_000 - 3 * 35_000)
print(3.14159 * 7**2)
print(f"Mỗi người: {100 // 7} viên, còn dư: {100 % 7} viên")
print(f"37°C = {37 * 9 / 5 + 32}°F")
```

Giải thích:
- Phép toán cơ bản: `+` (cộng), `-` (trừ), `*` (nhân), `/` (chia thường, kết quả luôn ra số thập phân dạng float).
- Lũy thừa (số mũ): dùng hai dấu sao `**`. Ví dụ `7**2` nghĩa là 7 mũ 2 (bằng 49). Phép lũy thừa được ưu tiên tính trước phép nhân và chia.
- Chia lấy phần nguyên `//`: ví dụ `100 // 7` được 14. Phép này bỏ hẳn phần thập phân, chỉ giữ lại số nguyên.
- Chia lấy phần dư `%`: ví dụ `100 % 7` được 2 (vì 7 nhân 14 bằng 98, còn dư 2).
- Dấu gạch dưới trong số: ví dụ viết `150_000` thì Python vẫn hiểu là `150000`. Dấu gạch dưới chỉ để người đọc dễ nhìn các hàng nghìn, triệu, không làm ảnh hưởng đến phép tính.

---

### Bài 3: Nhận dữ liệu từ bàn phím và ép kiểu (ex03_input.py)

Mục đích bài này là nhận thông tin do người dùng gõ vào và xử lý.

Code:
```python
# 1. Nhận tên dạng chữ
name = input("Bạn tên là gì? ").strip()
print(f"Xin chào, {name}!")

# 2. Nhận tuổi và đổi sang số nguyên để tính năm sinh
age = int(input("Bạn bao nhiêu tuổi? "))
print(f"Năm sinh ước tính: {2026 - age}")

# 3. Nhận 2 số thực và tính tổng
first = float(input("Nhập số thứ nhất: "))
second = float(input("Nhập số thứ hai: "))
print(f"Tổng: {first} + {second} = {first + second}")

# 4. Trò chơi ghép từ (Mad Libs)
n = input("Nhập tên: ").strip()
adj = input("Nhập tính từ: ").strip()
pet = input("Nhập con vật: ").strip()
num = input("Nhập một số: ").strip()
print(f"{n} có một con {pet} rất {adj}. Mỗi ngày nó ăn {num} bát cơm!")
```

Giải thích:
- `input("Lời nhắc: ")`: chương trình sẽ dừng lại chờ người dùng gõ chữ từ bàn phím và nhấn Enter.
- `.strip()`: cắt bỏ các khoảng trắng thừa ở hai đầu chuỗi nếu người dùng lỡ tay bấm phím cách (space).
- Ép kiểu dữ liệu:
  - `int(...)`: biến chuỗi chữ số thành số nguyên. Dùng cho tuổi tác, số lượng.
  - `float(...)`: biến chuỗi chữ số thành số thực (có dấu chấm thập phân). Dùng cho điểm số, tiền tệ, số đo.
- f-string (`f"..."`): thêm chữ `f` ở đầu chuỗi, sau đó có thể đặt tên biến hoặc biểu thức tính toán trực tiếp vào trong cặp ngoặc nhọn `{...}`. Cách này giúp ghép chữ và số rất tự nhiên, không cần chuyển đổi kiểu thủ công.

---

### Mini-project: Vẽ khung chữ tự động co dãn (mini-project/starter.py)

Mục đích: Viết chương trình nhận tên bất kỳ, sau đó vẽ một cái khung bao quanh tên đó. Tên dài hay ngắn thì khung cũng phải tự động co dãn theo cho vừa vặn.

Code:
```python
# Bước 1: Nhập tên
ten = input("Nhập tên của bạn: ").strip()

# Bước 2: Tính độ rộng khung
width = max(len(ten), 16) + 4
border = "═" * width

# Bước 3, 4, 5: In khung và nội dung căn giữa
print(f"╔{border}╗")
print(f"║{'Xin chào'.center(width)}║")
print(f"║{ten.upper().center(width)}║")
print(f"║{'🐍 Python Journey 🐍'.center(width)}║")
print(f"╚{border}╝")
```

Giải thuật:
1. Đo chiều dài tên: dùng hàm `len(ten)`. Nếu tên là "Vũ" thì độ dài là 2, nếu tên dài hơn thì số này tăng lên.
2. Tính độ rộng khung (`width`):
   - Trong khung có câu cố định "🐍 Python Journey 🐍" (dài khoảng 16 ký tự). Nếu người dùng nhập tên quá ngắn (ví dụ chỉ 2-3 chữ), khung vẫn cần rộng tối thiểu 16 ký tự để dòng khẩu hiệu không bị tràn viền. Vì vậy ta dùng `max(len(ten), 16)`.
   - Cộng thêm 4 ký tự nữa để tạo khoảng trống lề hai bên, chữ không bị dính sát mép khung.
3. Tạo thanh ngang: Python cho phép lấy một ký tự nhân với một số để tạo chuỗi lặp lại. `"═" * width` sẽ tạo ra một hàng ngang có đúng số lượng dấu gạch bằng với độ rộng đã tính.
4. Căn chữ vào giữa: dùng phương thức `.center(width)`. Python sẽ tự động chèn khoảng trắng đều sang hai bên trái và phải của từ để từ đó nằm ngay chính giữa dòng.

---

## 3. Ba lỗi hay gặp nhất của người mới học

1. Lỗi cộng chữ thay vì cộng số:
   - Nếu viết: `a = input()` rồi lấy `a + b`, khi nhập số 5 và 10, màn hình sẽ in ra `510` chứ không phải `15`.
   - Lý do: Python coi `a` và `b` là hai đoạn văn bản, phép cộng `+` đối với chữ là nối chữ lại với nhau. Phải bọc `int()` hoặc `float()` vào thì mới tính toán được.

2. Lỗi nhập chữ vào ô cần số:
   - Nếu chương trình có lệnh `age = int(input())` mà người dùng gõ chữ "hai mươi", Python sẽ dừng ngay lập tức và báo lỗi `ValueError` vì không thể đổi chữ "hai mươi" thành số được. (Cách xử lý lỗi này sẽ học kỹ ở Tuần 11 về Exception).

3. Lỗi tiếng Việt trên terminal Windows:
   - Terminal Windows cũ đôi khi không in được chữ tiếng Việt có dấu và báo lỗi `UnicodeEncodeError`.
   - Cách sửa: trong cửa sổ PowerShell, gõ `$env:PYTHONUTF8 = "1"` rồi mới chạy file python.
