# Tổng kết kiến thức Tuần 05: Danh sách (List) và Bộ giá trị (Tuple)

- Sinh viên: Lê Thanh Phi Vũ
- MSSV: 2123110178
- Môn học: Lập trình Python

---

## 1. Sự khác biệt cốt lõi giữa List và Tuple

| Tiêu chí | List (Danh sách) | Tuple (Bộ giá trị) |
|:---|:---|:---|
| **Ký hiệu** | Dấu ngoặc vuông `[1, 2, 3]` | Dấu ngoặc tròn `(1, 2, 3)` |
| **Tính thay đổi (Mutability)** | **Mutable (Có thể sửa đổi):** Thêm, sửa, xóa phần tử tùy thích sau khi tạo. | **Immutable (Bất biến):** Một khi đã tạo ra là cố định, không thể thêm bớt sửa xóa. |
| **Khi nào nên dùng?** | Khi danh sách dữ liệu cần cập nhật liên tục (giỏ hàng, danh sách công việc). | Khi dữ liệu mang tính chất cố định cần bảo vệ (tọa độ x, y, ngày tháng năm sinh, màu sắc RGB). Chạy nhanh hơn và an toàn hơn. |

---

## 2. Chi tiết bài tập, giải thuật và mô tả code

### Bài 1: Bốn thao tác cơ bản CRUD trên List (ex01_lists.py)

Code:
```python
subjects = ["Toán", "Văn", "Anh"]

# 1. Thêm phần tử
subjects.append("Lý")        # Thêm vào cuối danh sách
subjects.insert(1, "Hóa")    # Chèn vào vị trí số 1 (sau môn Toán)

# 2. Sửa phần tử
subjects[0] = "Toán Cao Cấp" # Gán đè giá trị mới vào vị trí số 0

# 3. Xóa phần tử
subjects.remove("Văn")       # Tìm đúng chữ 'Văn' và xóa
last = subjects.pop()        # Xóa phần tử cuối cùng và lấy ra dùng

# 4. Đọc phần tử và cắt lát
print("Phần tử đầu:", subjects[0])
print("Phần tử cuối:", subjects[-1])
print("Phần tử giữa:", subjects[1:-1])
```

Giải thích:
- `.append()` luôn thêm vào đuôi của danh sách.
- `.insert(vị_trí, giá_trị)` giúp chèn phần tử vào đúng chỗ mong muốn, các phần tử phía sau sẽ tự động lùi về sau 1 ô.
- Phân biệt `.remove()` và `.pop()`:
  - Dùng `.remove("Văn")` khi biết tên giá trị cần xóa.
  - Dùng `.pop()` khi muốn xóa theo vị trí (mặc định xóa phần tử cuối cùng) và lưu lại giá trị đó vào một biến để dùng tiếp.

---

### Bài 2: Bẫy sao chép danh sách (Alias vs Copy) (ex02_slicing.py)

Code:
```python
numbers = [1, 2, 3, 4, 5, 6]

# Cắt 3 số đầu và 3 số cuối
first_three = numbers[:3]
last_three = numbers[-3:]

# Bẫy gán bằng (Alias) vs Bản sao độc lập (Copy)
alias = numbers           # Đây CHỈ là đặt thêm tên gọi khác
copied = numbers.copy()   # Đây MỚI là tạo ra danh sách mới độc lập

alias.append(7)

print(first_three, last_three, alias, copied)
```

Giải thích - Cực kỳ quan trọng:
- Khi viết `alias = numbers`: Python **KHÔNG hề nhân đôi danh sách**. Nó chỉ tạo ra một cái tên mới cùng trỏ vào một vùng nhớ duy nhất. Do đó, khi bạn thêm số `7` vào `alias`, danh sách gốc `numbers` cũng bị thêm số `7` theo!
- Muốn tạo một bản sao độc lập (sửa bên này không ảnh hưởng bên kia), bắt buộc phải dùng lệnh `copied = numbers.copy()` hoặc dùng slicing `copied = numbers[:]`.

---

### Bài 3: Tuple và kỹ thuật Unpacking (ex03_tuples.py)

Code:
```python
# 1. Mở gói tọa độ (Unpacking)
coordinate = (3, 7)
x, y = coordinate
print(f"x = {x}, y = {y}")

# 2. Đóng gói (Packing) hồ sơ sinh viên
profile = ("Lê Thanh Phi Vũ", 20, "Python")
ten, tuoi, mon = profile

# 3. Đổi chỗ 2 biến bằng unpacking
left = "A"
right = "B"
left, right = right, left

print(x, y, profile, left, right)
```

Giải thích:
- Kỹ thuật Unpacking (Mở gói): Python cho phép lấy từng giá trị trong Tuple và gán lần lượt vào các biến riêng lẻ `x, y = coordinate` chỉ bằng đúng 1 câu lệnh.
- Số lượng biến bên trái phải bằng đúng số lượng phần tử của Tuple, nếu lệch sẽ bị báo lỗi `ValueError: too many values to unpack`.
- Phép đổi chỗ `left, right = right, left` bản chất chính là Python tự động đóng gói vế phải thành một Tuple tạm thời rồi mở gói vào 2 biến vế trái.

---

### Mini-project: Quản lý danh sách công việc (mini-project/starter.py)

Code:
```python
tasks = [("Learn lists", "done"), ("Observe mutability", "doing")]
tasks.append(("Practice unpacking", "todo"))

first_title, first_status = tasks[0]
print(f"first={first_title}, status={first_status}")

copied_tasks = tasks.copy()
tasks[1] = ("Observe mutability", "done")

print(f"current={tasks}")
print(f"copy={copied_tasks}")
```

Giải thích:
- Kết hợp List và Tuple: Mỗi công việc là một Tuple cố định gồm `(tên_việc, trạng_thái)`. Toàn bộ công việc được đặt trong một List để có thể thêm, sửa, xóa linh hoạt.
- Dùng `tasks.copy()` giúp lưu lại trạng thái trước đó của danh sách để theo dõi sự thay đổi.

---

## 3. Những lỗi dễ mắc phải nhất trong Tuần 05

1. Nhầm lẫn `alias = a` là đã sao chép:
   - Thay đổi `alias` làm biến `a` bị đổi theo ngoài ý muốn. Luôn nhớ dùng `.copy()`.
2. Cố gắng thay đổi phần tử của Tuple:
   - Viết `t = (1, 2)` rồi gán `t[0] = 10` sẽ bị báo lỗi `TypeError: 'tuple' object does not support item assignment`. Nếu cần thay đổi dữ liệu thì phải dùng List `[]`.
3. Xóa phần tử không tồn tại bằng `.remove()`:
   - Gọi `subjects.remove("Lịch Sử")` khi trong danh sách không có môn Lịch Sử sẽ làm chương trình bị dừng ngay lập tức với lỗi `ValueError: list.remove(x): x not in list`.
