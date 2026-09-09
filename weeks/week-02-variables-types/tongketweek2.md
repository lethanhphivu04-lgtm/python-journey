# Tổng kết kiến thức Tuần 02: Biến, kiểu dữ liệu và ép kiểu

- Sinh viên: Lê Thanh Phi Vũ
- MSSV: 2123110178
- Môn học: Lập trình Python

---

## 1. Bốn kiểu dữ liệu cơ bản nhất trong Python

1. `str` (String - Chuỗi): Dùng để chứa văn bản, chữ cái. Luôn được đặt trong dấu ngoặc kép hoặc ngoặc đơn (ví dụ: `"Lê Thanh Phi Vũ"`, `'2123110178'`).
2. `int` (Integer - Số nguyên): Các số nguyên không có phần thập phân, có thể âm, dương hoặc bằng 0 (ví dụ: `20`, `-5`, `0`).
3. `float` (Số thực): Các số có phần thập phân sau dấu chấm (ví dụ: `8.5`, `3.14159`).
4. `bool` (Boolean - Đúng/Sai): Chỉ có đúng 2 giá trị là `True` hoặc `False` (lưu ý chữ cái đầu phải viết hoa).

Để kiểm tra xem một biến đang thuộc kiểu gì, dùng lệnh `type(tên_biến)`.

---

## 2. Chi tiết bài tập, giải thuật và mô tả code

### Bài 1: Khai báo biến và các phép gán (ex01_variables.py)

Code:
```python
# 1. Khai báo 4 kiểu dữ liệu
ten = "Lê Thanh Phi Vũ"
tuoi = 20
diem_tb = 8.5
dang_hoc = True
print(f"ten: {ten} ({type(ten)})")
print(f"tuoi: {tuoi} ({type(tuoi)})")
print(f"diem_tb: {diem_tb} ({type(diem_tb)})")
print(f"dang_hoc: {dang_hoc} ({type(dang_hoc)})")

# 2. Đổi chỗ giá trị 2 biến
a = 10
b = 20
a, b = b, a
print(f"a = {a}, b = {b}")

# 3. Phép gán tăng giảm nhanh (Augmented Assignment)
x = 100
x += 50   # tương đương x = x + 50 -> ra 150
x -= 20   # tương đương x = x - 20 -> ra 130
x *= 2    # tương đương x = x * 2  -> ra 260
x //= 4   # tương đương x = x // 4 -> ra 65

# 4. Gán nhiều biến trên cùng một dòng
ho, ten, tuoi = "Lê Thanh", "Phi Vũ", 20
print(f"Họ tên: {ho} {ten}, {tuoi} tuổi")
```

Giải thích:
- Đổi chỗ `a, b = b, a`: Ở các ngôn ngữ khác như C hay Java, bạn phải tạo thêm một biến tạm `temp` để giữ giá trị rồi mới đổi được. Trong Python, ta chỉ cần viết `a, b = b, a` là hai biến tự đổi giá trị cho nhau ngay lập tức.
- Các phép `+=`, `-=`, `*=`, `//=`: Giúp viết code ngắn hơn. Thay vì viết `x = x + 50`, ta viết gọn lại là `x += 50`.
- Gán nhiều biến `ho, ten, tuoi = ...`: Số lượng biến bên trái dấu bằng phải khớp chính xác với số lượng giá trị bên phải dấu bằng.

---

### Bài 2: Chuyển đổi kiểu dữ liệu (ex02_type_conversion.py)

Code:
```python
# 1. Đổi chữ thành số nguyên
so_text = "42"
print("Kết quả:", int(so_text) + 8)  # Ra 50

# 2. Đổi số thực sang số nguyên
pi = 3.14159
print("pi sang int:", int(pi))      # Ra 3

# 3. Kiểm tra tính Đúng/Sai của các giá trị
print(bool(0), bool(1), bool(""), bool("hello"), bool([]), bool([1, 2]))
# Kết quả: False True False True False True

# 4. Tính chỉ số BMI
chieu_cao = float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))
bmi = can_nang / (chieu_cao ** 2)
print(f"BMI: {bmi:.1f}")

# 5. Đổi số giây sang giờ, phút, giây
tong_giay = int(input("Nhập số giây: "))
gio = tong_giay // 3600
phut = (tong_giay % 3600) // 60
giay = tong_giay % 60
print(f"{tong_giay} giây = {gio} giờ {phut} phút {giay} giây")
```

Giải thích:
- Ép kiểu `int(pi)`: Chú ý hàm `int()` khi ép số thực sẽ cắt bỏ toàn bộ phần sau dấu chấm (3.14159 còn 3), chứ nó không làm tròn số. Nếu muốn làm tròn toán học phải dùng hàm `round()`.
- Cơ chế `bool()` (Truthy và Falsy): Trong Python, cái gì rỗng hoặc mang số 0 thì mang giá trị `False` (như số `0`, chuỗi rỗng `""`, danh sách rỗng `[]`). Bất kỳ cái gì có chứa dữ liệu hoặc khác 0 thì đều là `True`.
- Định dạng `{bmi:.1f}`: Dấu `:.1f` nghĩa là chỉ lấy 1 chữ số ở phần thập phân sau dấu chấm.
- Thuật toán đổi giây sang giờ/phút/giây:
  1. 1 giờ có 3600 giây -> lấy tổng số giây chia nguyên cho 3600 để ra số giờ: `tong_giay // 3600`.
  2. Số giây còn sót lại sau khi đổi ra giờ là `tong_giay % 3600`.
  3. Lấy số giây còn sót này chia nguyên cho 60 để ra số phút: `(tong_giay % 3600) // 60`.
  4. Số giây lẻ cuối cùng là phép chia dư cho 60: `tong_giay % 60`.

---

### Bài 3: Máy tính kết hợp nhận input (ex03_input_calc.py)

Code:
```python
# 1. Bốn phép tính cơ bản
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
print(f"Tổng: {a + b}, Hiệu: {a - b}, Tích: {a * b}, Thương: {a / b}")

# 2. Diện tích và chu vi hình tròn
r = float(input("Nhập bán kính r: "))
pi = 3.14159
print(f"Diện tích: {pi * r**2:.2f}, Chu vi: {2 * pi * r:.2f}")

# 3. Tính tiền sau khi giảm giá
gia_goc = float(input("Nhập giá gốc: "))
giam_gia = float(input("Nhập % giảm giá: "))
gia_sau_giam = gia_goc * (1 - giam_gia / 100)
print(f"Giá sau giảm: {gia_sau_giam:,.0f} VNĐ")

# 4. Đổi tiền tệ
vnd = float(input("Nhập số tiền VNĐ: "))
ty_gia = float(input("Nhập tỷ giá USD/VNĐ: "))
print(f"Số USD: {vnd / ty_gia:.2f} USD")
```

Giải thích:
- Dùng `float(input())`: Thay vì `int()`, dùng `float()` giúp người dùng có thể nhập được cả số nguyên lẫn số có dấu chấm thập phân (ví dụ bán kính 2.5).
- Định dạng tiền tệ `{gia_sau_giam:,.0f}`: Dấu phẩy `,` tự động thêm dấu phân cách hàng nghìn (ví dụ 400000 thành 400,000), `.0f` nghĩa là không lấy số thập phân.

---

### Mini-project: Thẻ sinh viên (mini-project/starter.py)

Mục đích: Nhập thông tin sinh viên, kiểm tra dữ liệu đầu vào (không để trống, năm nhập học đúng 4 chữ số), tính năm tốt nghiệp và in thẻ.

Code:
```python
while True:
    name = input("Họ tên: ").strip()
    if name:
        break
    print("Họ tên không được rỗng, vui lòng nhập lại!")

while True:
    student_id = input("Mã sinh viên: ").strip()
    if student_id:
        break
    print("Mã sinh viên không được rỗng, vui lòng nhập lại!")

while True:
    major = input("Ngành: ").strip()
    if major:
        break
    print("Ngành không được rỗng, vui lòng nhập lại!")

while True:
    start_year_text = input("Năm nhập học: ").strip()
    if start_year_text.isdigit() and len(start_year_text) == 4:
        break
    print("Năm nhập học cần là số có 4 chữ số (ví dụ 2023), vui lòng nhập lại!")

start_year = int(start_year_text)
graduation_year = start_year + 4
print(f"{name} · {student_id} · {major}")
print(f"Khóa: {start_year}–{graduation_year}")
```

Giải thuật:
1. Nhận thông tin: dùng `.strip()` để xóa các khoảng trắng thừa ở hai đầu chuỗi.
2. Kiểm tra chuỗi rỗng: `if name:` kiểm tra nếu có nội dung thì `break` đi tiếp, nếu để trống thì bắt nhập lại ngay, không cho đi qua.
3. Kiểm tra năm nhập học:
   - Dùng `start_year_text.isdigit()` kết hợp `len(start_year_text) == 4`.
   - Đảm bảo người dùng phải nhập đúng 4 chữ số (như `2023`) thì mới gọi hàm `int()`, tránh hoàn toàn lỗi sập chương trình (`ValueError`).
4. Năm tốt nghiệp dự kiến: Lấy `start_year + 4`.

---

## 3. Năm lưu ý lý thuyết quan trọng (ít ai để ý) trong Tuần 02

1. **Phép chia `/` luôn luôn trả về số thực (`float`):**
   - Kể cả khi chia hết hoàn toàn: `10 / 2` sẽ ra `5.0` chứ **không phải** `5`.
   - Muốn lấy số nguyên `5`, bắt buộc phải dùng phép chia lấy nguyên: `10 // 2`.

2. **Sai số dấu phẩy động: `0.1 + 0.2 != 0.3`:**
   - Trong máy tính, `print(0.1 + 0.2)` sẽ in ra `0.30000000000000004`.
   - Nguyên nhân: Máy tính biểu diễn số ở hệ nhị phân (0 và 1), nên một số số thập phân bị tuần hoàn vô hạn không thể lưu chính xác tuyệt đối.
   - Khi so sánh số thực, nên dùng `round(0.1 + 0.2, 2) == 0.3`.

3. **Viết số lớn dễ nhìn bằng dấu gạch dưới `_`:**
   - Thay vì viết `1000000000` rất dễ hoa mắt, Python cho phép viết `1_000_000_000` (1 tỷ). Python tự động bỏ qua dấu gạch dưới này.

4. **Kiểu `bool` thực chất là con của kiểu `int`:**
   - `True` có giá trị là `1`, `False` có giá trị là `0`.
   - Vì thế `True + True` ra `2`, `True * 5` ra `5`. Hàm kiểm tra `isinstance(True, int)` sẽ trả về `True`.

5. **Quy tắc đặt tên biến và các từ khóa cấm kỵ:**
   - Tên biến chuẩn Python phải dùng `snake_case` (chữ thường, nối bằng gạch dưới: `ten_sinh_vien`).
   - Tuyệt đối không bắt đầu bằng số (sai: `2ten`), không dùng dấu gạch ngang (sai: `so-luong`).
   - Không được trùng với khoảng 35 từ khóa của Python (`if`, `else`, `for`, `while`, `def`, `class`, `import`, `return`, `True`, `False`...).

---

## 4. Những lỗi dễ mắc phải nhất trong Tuần 02

1. Ép kiểu chuỗi số thập phân trực tiếp sang int:
   - Nếu có chuỗi `"3.14"`, nếu bạn viết `int("3.14")`, Python sẽ báo lỗi ngay lập tức vì chuỗi chứa dấu chấm.
   - Cách làm đúng: Đổi sang float trước rồi mới đổi sang int: `int(float("3.14"))`.
2. Chia cho số 0:
   - Trong phép tính `a / b` hoặc `tong_giay % 60`, nếu số chia là 0, Python sẽ văng lỗi `ZeroDivisionError`. Luôn chú ý mẫu số phải khác 0.
3. Nhầm lẫn giữa dấu chấm và dấu phẩy khi gõ số thực:
   - Trong Python, số thập phân bắt buộc phải dùng dấu chấm `.` (ví dụ `3.14`, `1.75`). Nếu quen tay gõ dấu phẩy `,` (ví dụ `3,14`), Python sẽ hiểu đó là một tuple gồm 2 số riêng biệt chứ không phải một số thực.
