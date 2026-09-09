# Tổng kết kiến thức Tuần 03: Cấu trúc điều kiện và kiểm tra dữ liệu đầu vào

- Sinh viên: Lê Thanh Phi Vũ
- MSSV: 2123110178
- Môn học: Lập trình Python

---

## 1. Cốt lõi về câu lệnh điều kiện trong Python

- Cấu trúc rẽ nhánh gồm 3 từ khóa: `if` (nếu), `elif` (nếu không thì xét tiếp), và `else` (trường hợp còn lại cuối cùng).
- Quy tắc thụt đầu dòng (Indentation): Trong Python, sau dấu hai chấm `:` ở mỗi câu lệnh `if/elif/else`, các dòng code bên trong bắt buộc phải lùi vào 4 dấu cách (phím Tab). Thụt lề sai sẽ bị báo lỗi `IndentationError`.
- Phân biệt hai dấu bằng và một dấu bằng:
  - Dấu `=` là phép gán giá trị (ví dụ `tuoi = 18`).
  - Dấu `==` là phép so sánh bằng (ví dụ `if tuoi == 18:`).
- Ba toán tử logic quan trọng:
  - `and`: Cả 2 vế đều phải đúng thì kết quả mới đúng.
  - `or`: Chỉ cần 1 trong 2 vế đúng là kết quả đúng.
  - `not`: Đảo ngược trạng thái (đang đúng thành sai, đang sai thành đúng).

---

## 2. Chi tiết bài tập, giải thuật và mô tả code

### Bài 1: if / elif / else cơ bản (ex01_if_else.py)

Code:
```python
# 1. Phân loại độ tuổi
tuoi = int(input("Nhập tuổi: "))
if tuoi < 13:
    print("Thiếu nhi")
elif tuoi <= 17:
    print("Thiếu niên")
elif tuoi <= 64:
    print("Người lớn")
else:
    print("Người cao tuổi")

# 2. Xếp loại điểm học tập
diem = float(input("Nhập điểm (0-10): "))
if diem < 0 or diem > 10:
    print("Không hợp lệ")
elif diem >= 9:
    print("Xuất sắc")
elif diem >= 8:
    print("Giỏi")
elif diem >= 6.5:
    print("Khá")
elif diem >= 5:
    print("TB")
else:
    print("Yếu")

# 3. Kiểm tra năm nhuận
nam = int(input("Nhập năm: "))
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print("Năm nhuận")
else:
    print("Không phải năm nhuận")

# 4. Tìm số lớn nhất trong 3 số
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
if a >= b and a >= c:
    so_lon_nhat = a
elif b >= a and b >= c:
    so_lon_nhat = b
else:
    so_lon_nhat = c
print("Số lớn nhất:", so_lon_nhat)
```

Giải thích:
- Thứ tự kiểm tra từ trên xuống dưới:
  - Ở bài xếp loại điểm, ta chặn trường hợp điểm vô lý trước (`diem < 0 or diem > 10`).
  - Khi xét `elif diem >= 8:`, Python đã biết chắc chắn điểm nhỏ hơn 9 rồi (vì nếu >= 9 thì nó đã lọt vào nhánh Xuất sắc ở trên). Nhờ vậy code rất gọn, không cần viết rườm rà `8 <= diem < 9`.
- Thuật toán năm nhuận: Theo lịch dương, một năm là năm nhuận nếu:
  1. Năm đó chia hết cho 4 NHƯNG không chia hết cho 100 (`nam % 4 == 0 and nam % 100 != 0`), HOẶC
  2. Năm đó chia hết cho 400 (`nam % 400 == 0`).
  Ví dụ: năm 2000 là năm nhuận (chia hết cho 400), năm 1900 không phải năm nhuận (chia hết cho 100 nhưng không chia hết cho 400).
- Tìm số lớn nhất: So sánh từng số với 2 số còn lại bằng toán tử `and`.

---

### Bài 2: Toán tử logic and, or, not (ex02_logical.py)

Code:
```python
# 1. Điều kiện lái xe
tuoi = int(input("Tuổi: "))
co_bang_lai = input("Có bằng lái? (y/n): ").lower() == "y"
khong_say = input("Tỉnh táo? (y/n): ").lower() == "y"
if tuoi >= 18 and co_bang_lai and khong_say:
    print("Đủ điều kiện lái xe")
else:
    print("Không đủ điều kiện lái xe")

# 2. Phân loại tam giác
a = float(input("Cạnh a: "))
b = float(input("Cạnh b: "))
c = float(input("Cạnh c: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Tam giác đều")
    elif a == b or b == c or a == c:
        print("Tam giác cân")
    else:
        print("Tam giác thường")
else:
    print("Không phải tam giác")

# 3. Kiểm tra mật khẩu mạnh
pw = input("Nhập mật khẩu: ")
if (
    len(pw) >= 8
    and any(c.isupper() for c in pw)
    and any(c.islower() for c in pw)
    and any(c.isdigit() for c in pw)
):
    print("Mật khẩu mạnh")
else:
    print("Mật khẩu yếu")

# 4. Trò chơi FizzBuzz
n = int(input("Nhập số n: "))
if n % 15 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
```

Giải thích:
- Định lý tam giác: 3 đoạn thẳng chỉ tạo thành một tam giác khi tổng độ dài của 2 cạnh bất kỳ luôn lớn hơn cạnh thứ ba. Nếu không thỏa mãn điều kiện này, in ra ngay "Không phải tam giác".
- Kiểm tra mật khẩu bằng hàm `any()`:
  - `any(c.isupper() for c in pw)` nghĩa là: "xem qua từng ký tự trong mật khẩu, chỉ cần có ít nhất 1 chữ hoa thì đúng".
  - Tương tự với chữ thường `c.islower()` và chữ số `c.isdigit()`.
- Bẫy kinh điển trong bài FizzBuzz:
  - Chia hết cho cả 3 và 5 tức là chia hết cho 15 (`n % 15 == 0`).
  - Bắt buộc phải đưa điều kiện `n % 15 == 0` lên đầu tiên. Nếu để `n % 3 == 0` lên đầu, khi nhập số 15, máy sẽ thấy 15 chia hết cho 3 và in ra "Fizz" rồi kết thúc luôn, không bao giờ in được chữ "FizzBuzz".

---

### Bài 3: Điều kiện lồng nhau và máy bán vé (ex03_nested.py)

Code:
```python
# 1. Rút tiền ATM
so_du = float(input("Số dư hiện tại: "))
tien_rut = float(input("Số tiền muốn rút: "))
if tien_rut <= 0:
    print("Số tiền rút phải lớn hơn 0")
elif tien_rut > so_du:
    print("Số dư không đủ")
elif tien_rut % 50_000 != 0:
    print("Số tiền rút phải là bội số của 50,000 VNĐ")
else:
    so_du -= tien_rut
    print(f"Rút tiền thành công! Số dư còn lại: {so_du:,.0f} VNĐ")

# 2. Xếp loại BMI
h = float(input("Chiều cao (m): "))
w = float(input("Cân nặng (kg): "))
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

# 3. Giá vé xem phim
loai_ve = input("Loại vé (thuong/vip): ").strip().lower()
ngay = input("Ngày xem (thuong/cuoi_tuan): ").strip().lower()
tuoi = int(input("Tuổi: "))

# Dùng toán tử 3 ngôi gán giá gốc
gia = 120_000 if loai_ve == "vip" else 80_000

# Nếu cuối tuần thì tăng 30% giá
if ngay == "cuoi_tuan":
    gia *= 1.3

# Giảm giá theo độ tuổi
if tuoi < 12 or tuoi >= 65:
    gia *= 0.5   # Trẻ em và người cao tuổi giảm 50%
elif 18 <= tuoi <= 25:
    gia *= 0.8   # Sinh viên giảm 20%

print(f"Giá vé cuối cùng: {gia:,.0f} VNĐ")
```

Giải thích:
- Kỹ thuật chặn lỗi từng bước (Guards) ở bài ATM:
  - Thay vì lồng nhiều lớp `if` vào trong nhau rất rối mắt, ta kiểm tra các trường hợp vi phạm lần lượt từ trên xuống dưới: rút số âm -> rút quá số dư -> rút số lẻ không chia hết cho 50k. Vượt qua hết tất cả các rào chắn này thì mới cho rút tiền.
- Toán tử 3 ngôi (Ternary Operator): `gia = 120_000 if loai_ve == "vip" else 80_000`. Nghĩa là: nếu chọn vé vip thì giá là 120k, ngược lại giá là 80k. Viết gọn gàng trong đúng 1 dòng.

---

### Mini-project: Kiểm tra dữ liệu đầu vào vé xem phim (mini-project/starter.py)

Mục đích: Không tin tưởng bất kỳ thứ gì người dùng nhập vào. Luôn kiểm tra tính hợp lệ trước khi quyết định in vé.

Code:
```python
while True:
    # 1. Nhập tên (không để trống)
    while True:
        name = input("Tên: ").strip()
        if name:
            break
        print("Tên không được để trống, vui lòng nhập lại!")

    # 2. Nhập tuổi (phải là số nguyên không âm từ 0 đến 120)
    while True:
        age_text = input("Tuổi: ").strip()
        if age_text.isdigit():
            age = int(age_text)
            if 0 <= age <= 120:
                break
            print("Tuổi phải nằm trong khoảng 0 đến 120, vui lòng nhập lại!")
        else:
            print("Tuổi cần là số nguyên không âm, vui lòng nhập lại!")

    # 3. Nhập loại vé (chỉ nhận standard hoặc vip)
    while True:
        ticket_type = input("Loại vé (standard/vip): ").strip().lower()
        if ticket_type in ("standard", "vip"):
            break
        print("Loại vé chỉ nhận 'standard' hoặc 'vip', vui lòng nhập lại!")

    # 4. Phân loại vé và in kết quả
    if age < 12:
        print(f"{name}: vé trẻ em")
    elif ticket_type == "vip":
        print(f"{name}: vé VIP")
    else:
        print(f"{name}: vé standard")

    # 5. Hỏi người dùng muốn nhập tiếp không để tránh văng chương trình
    tiep_tuc = input("\nBạn có muốn nhập vé tiếp theo không? (y/n): ").strip().lower()
    if tiep_tuc != "y":
        print("Đã kết thúc chương trình kiểm tra vé.")
        break
    print("-" * 35)
```

Giải thuật:
1. `while True:` cho từng ô nhập: Khi người dùng gõ sai (ví dụ tuổi gõ chữ "ed", hoặc loại vé gõ "de"), chương trình không dừng hay văng ra màn hình lệnh (terminal) mà in thông báo lỗi rõ ràng và yêu cầu nhập lại đúng ô đó cho đến khi hợp lệ (`break`).
2. `name.strip()` và `if name:`: Loại bỏ khoảng trắng thừa, nếu người dùng chỉ nhấn Enter thì bắt nhập lại.
3. `age_text.isdigit()` và `0 <= age <= 120`: Đảm bảo tuổi là số nguyên không âm và hợp lý về mặt sinh học.
4. `ticket_type in ("standard", "vip")`: Chỉ chấp nhận đúng 2 loại vé được quy định.
5. Vòng lặp ngoài cùng: Sau khi in vé xong, hỏi người dùng có muốn nhập tiếp vé cho người khác không (`y/n`). Nếu không thì thoát ra một cách lịch sự, không bị thoát đột ngột.

---

## 3. Ba lỗi hay gặp nhất của người mới học trong Tuần 03

1. Nhầm lẫn giữa `=` và `==`:
   - Lỗi kinh điển: `if a = 10:` -> Python sẽ báo lỗi cú pháp `SyntaxError` vì dấu `=` là gán chứ không phải so sánh. Phải viết đúng là `if a == 10:`.
2. Sai thứ tự rẽ nhánh:
   - Đặt điều kiện rộng lên trước điều kiện hẹp (như trường hợp bài FizzBuzz).
3. Quên thụt lề:
   - Quên bấm Tab hoặc thụt dòng không đều nhau sau dấu hai chấm `:` khiến chương trình báo lỗi `IndentationError`.
