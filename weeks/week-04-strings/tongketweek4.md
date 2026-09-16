# Tổng kết kiến thức Tuần 04: Xử lý chuỗi và Regex cơ bản

- Sinh viên: Lê Thanh Phi Vũ
- MSSV: 2123110178
- Môn học: Lập trình Python

---

## 1. Bản chất của chuỗi (String) trong Python

- Chuỗi là một dãy ký tự có thứ tự, bắt đầu đếm từ vị trí `0`.
- Chuỗi trong Python có tính chất bất biến (Immutable): Một khi đã tạo ra chuỗi thì không thể gán đè một ký tự con (ví dụ không thể viết `s[0] = 'A'`). Muốn thay đổi ta phải tạo ra chuỗi mới.
- Cú pháp cắt chuỗi (Slicing): `chuoi[bắt_đầu : kết_thúc : bước_nhảy]`
  - Vị trí `kết_thúc` không được lấy (chỉ lấy đến trước nó 1 ký tự).
  - Bước nhảy âm `-1` dùng để đảo ngược chuỗi: `chuoi[::-1]`.

---

## 2. Chi tiết bài tập, giải thuật và mô tả code

### Bài 1: Cắt chuỗi và chỉ số (ex01_indexing.py)

Code:
```python
s = "Python Journey"
print("Ký tự đầu:", s[0])        # 'P'
print("Ký tự cuối:", s[-1])      # 'y'
print("5 ký tự đầu:", s[:5])     # 'Pytho'

print("a)", s[7:])               # 'Journey'
print("b)", s[::-1])             # Đảo ngược toàn bộ
print("c)", s[::2])              # Lấy cách 1 ký tự

# Cắt mã CCCD
cccd = input("Nhập CCCD (12 chữ số): ").strip()
print(f"Mã tỉnh: {cccd[:3]}, Giới tính: {cccd[3]}, Năm sinh: {cccd[4:6]}")

# Kiểm tra chuỗi đối xứng (Palindrome)
text = input("Nhập chuỗi kiểm tra palindrome: ").strip()
clean = "".join(text.lower().split())
print("Đối xứng:", clean == clean[::-1])
```

Giải thích:
- Chỉ số âm: Số `-1` là ký tự cuối cùng, `-2` là áp chót. Rất tiện vì không cần phải tính `len(s) - 1`.
- Thuật toán Palindrome: Chuỗi đối xứng là chuỗi đọc xuôi hay ngược đều như nhau (ví dụ: "racecar"). Ta chỉ cần so sánh chuỗi đã làm sạch `clean` với chuỗi đảo ngược của nó `clean[::-1]`.

---

### Bài 2: Các phương thức xử lý chuỗi có sẵn (ex02_methods.py)

Code:
```python
# 1. Chuẩn hóa email
email = "  User@Example.COM  "
print(email.strip().lower())

# 2. Xử lý đoạn văn
sentence = "hello world python programming"
print("a)", sentence.title())                           # Viết Hoa Chữ Đầu Mỗi Từ
print("b)", sentence.count("o"))                        # Đếm số chữ o xuất hiện
print("c)", sentence.replace("python", "PYTHON"))       # Thay thế từ

# 3. Tách họ và tên
ho_ten = input("Nhập họ tên đầy đủ: ").strip()
parts = ho_ten.split()
ho = parts[0] if parts else ""
ten = parts[-1] if len(parts) > 1 else ho
print(f"Họ: {ho}, Tên: {ten}")

# 4. Kiểm tra đuôi file
filename = input("Nhập tên file: ").strip().lower()
print("Hợp lệ:", filename.endswith((".py", ".txt", ".csv")))

# 5. Mã hóa Caesar
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
```

Giải thích:
- `.split()`: Cắt chuỗi thành một danh sách các từ dựa trên khoảng trắng. Lấy từ đầu tiên `parts[0]` là Họ, lấy từ cuối cùng `parts[-1]` là Tên.
- `.endswith((...))`: Kiểm tra đuôi file có thuộc một trong các định dạng cho phép hay không. Có thể truyền vào một tuple gồm nhiều đuôi cùng lúc.
- Mã hóa Caesar: Thuật toán dịch chuyển chữ cái trong bảng mã ASCII. Dùng `ord(c)` để lấy mã số của chữ và `chr(...)` để chuyển mã số ngược lại thành chữ. Phép `% 26` giúp khi dịch quá chữ Z sẽ tự động quay vòng lại chữ A.

---

### Bài 3: Căn chỉnh giao diện văn bản bằng f-string (ex03_fstrings.py)

Code:
```python
# 1. Định dạng số thập phân
ten = "An"
tuoi = 20
diem = 8.567
print(f"Học sinh {ten}, {tuoi} tuổi, điểm TB: {diem:.2f}")

# 2. Bảng cửu chương thẳng cột
for i in range(1, 11):
    print(f"5 x {i:>2} = {5 * i:>3}")

# 3. In hóa đơn căn lề trái/phải
print("===========================")
print(f"{'SẢN PHẨM':<15}{'GIÁ (VNĐ)':>12}")
print("---------------------------")
print(f"{'Cà phê':<15}{35_000:>12,}")
print(f"{'Bánh mì':<15}{25_000:>12,}")
print(f"{'Nước suối':<15}{10_000:>12,}")
print("---------------------------")
print(f"{'TỔNG CỘNG':<15}{70_000:>12,}")
print("===========================")

# 4. Thanh tiến trình (Progress Bar)
pct = int(input("Nhập phần trăm (0-100): "))
filled = int(pct / 100 * 20)
empty = 20 - filled
print(f"[{'█' * filled}{'░' * empty}] {pct}%")
```

Giải thích:
- `:<15`: Căn lề trái, dành độ rộng 15 ô hiển thị.
- `:>12`: Căn lề phải, dành độ rộng 12 ô hiển thị (rất thích hợp cho cột số tiền).
- `:,`: Tự động thêm dấu phẩy ngăn cách hàng nghìn.
- Thanh tiến trình: Chia tổng độ dài thanh thành 20 ô vuông. Lấy phần trăm nhân với 20 để biết cần vẽ bao nhiêu ô đầy `█` và bao nhiêu ô rỗng `░`.

---

### Bài 4 & Mini-project: Biểu thức chính quy Regex và Phân tích văn bản

Code:
```python
import re

text = "Tickets PJ-101 and PJ-205 are open; XX-999 is unrelated."

# Tìm tất cả mã có dạng PJ-xxx (với xxx là 3 chữ số)
codes = re.findall(r"PJ-\d{3}", text)

# Tìm chuỗi số đầu tiên
match = re.search(r"\d+", text)
first_number = match.group() if match else None

# Kiểm tra mã tuần hợp lệ (chữ W kèm 2 chữ số)
candidate = "W04"
is_week_code = bool(re.fullmatch(r"W\d{2}", candidate))

# 4. Mini-project: Phân tích văn bản (Text Analyzer)
text_input = input("Text: ").strip()
if not text_input:
    print("Text không được rỗng")
else:
    normalized = " ".join(text_input.lower().split())
    words = normalized.split()
    pj_codes = re.findall(r"PJ-\d{3}", text_input)
    print(f"normalized={normalized}")
    print(f"characters={len(normalized)}")
    print(f"words={len(words)}")
    print(f"python_count={normalized.count('python')}")
    print(f"course_codes={pj_codes}")
```

Giải thích:
- Khi nào dùng String Methods, khi nào dùng Regex:
  - Nếu chỉ tìm một từ cố định (ví dụ tìm xem có chữ "python" không), hãy dùng toán tử `in` hoặc `.find()`, đơn giản và chạy nhanh hơn rất nhiều.
  - Khi cần tìm một chuỗi có "quy luật" biến đổi (ví dụ: mã vé bắt đầu bằng `PJ-` theo sau là đúng 3 chữ số, số điện thoại, email), lúc đó mới cần dùng Regex.
- `\d`: đại diện cho 1 chữ số bất kỳ (0-9).
- `{3}`: lặp lại đúng 3 lần.
- `\d+`: có 1 hoặc nhiều chữ số liên tiếp.
- `re.findall()`: tìm và gom tất cả các đoạn khớp thành một danh sách.
- `re.fullmatch()`: bắt buộc toàn bộ chuỗi từ đầu đến cuối phải khớp chính xác với mẫu quy định.

---

## 3. Những lỗi thường gặp trong Tuần 04

1. Lỗi tưởng chuỗi bị thay đổi tại chỗ:
   - Viết `s.strip()` hoặc `s.replace("a", "b")` rồi tưởng `s` đã tự đổi. Chuỗi trong Python không thay đổi tại chỗ được, muốn lưu kết quả phải gán lại vào biến: `s = s.strip()`.
2. Lỗi tràn chỉ số (IndexError):
   - Chuỗi có 5 ký tự thì vị trí tối đa là 4. Gọi `s[5]` sẽ bị báo lỗi `string index out of range`. Dùng slicing `s[:5]` thì an toàn hơn vì không bao giờ báo lỗi này.
3. Lạm dụng Regex:
   - Những việc đơn giản như kiểm tra đuôi `.py` thì dùng `.endswith(".py")` là đủ, không cần mất công dùng Regex cho phức tạp.
