# Tổng kết kiến thức Tuần 06: Vòng lặp for, while và List Comprehension

- Sinh viên: Lê Thanh Phi Vũ
- MSSV: 2123110178
- Môn học: Lập trình Python

---

## 1. Cốt lõi về vòng lặp trong Python

- Vòng lặp giúp máy tính thực hiện các công việc lặp đi lặp lại một cách tự động.
- Khi nào dùng `for`? Khi đã biết trước số lần lặp (ví dụ lặp 10 lần bằng `range(10)`) hoặc muốn duyệt qua từng phần tử của một danh sách/chuỗi.
- Khi nào dùng `while`? Khi lặp dựa trên một điều kiện đúng/sai (chưa biết trước sẽ lặp bao nhiêu lần, cứ khi nào điều kiện còn `True` thì còn chạy).

---

## 2. Chi tiết bài tập, giải thuật và mô tả code

### Bài 1: Vòng lặp for, range, enumerate và zip (ex01_for_loop.py)

Code:
```python
topics = ["loops", "enumerate", "zip"]
scores = [7, 8, 9]

# 1. Dùng range in từ 1 đến 5
for i in range(1, 6):
    print(i)

# 2. Dùng enumerate lấy số thứ tự tự động
for idx, topic in enumerate(topics, start=1):
    print(f"{idx}. {topic}")

# 3. Dùng zip ghép đôi 2 danh sách chạy song song
for topic, score in zip(topics, scores, strict=True):
    print(f"{topic}: {score}")
```

Giải thích:
- `range(1, 6)`: Tạo ra dãy số từ 1 đến 5 (số kết thúc 6 không được lấy).
- `enumerate(topics, start=1)`: Thay vì phải tự tạo một biến đếm bên ngoài như `i = 1` rồi mỗi vòng lặp lại phải cộng `i += 1`, hàm `enumerate` tự động trả về cả số thứ tự `idx` lẫn giá trị `topic`. Rất sạch sẽ và không lo quên tăng biến đếm.
- `zip(topics, scores)`: Ghép từng phần tử ở vị trí tương ứng của 2 danh sách lại với nhau. Phần tử 1 đi với phần tử 1, phần tử 2 đi với phần tử 2. `strict=True` giúp cảnh báo lỗi nếu 2 danh sách có độ dài không bằng nhau.

---

### Bài 2: Vòng lặp while, break và continue (ex02_while_loop.py)

Code:
```python
remaining = 5

# 1. Đếm ngược về 1
while remaining > 0:
    print(remaining)
    remaining -= 1

# 2. Điều khiển vòng lặp với break và continue
num = 1
while num <= 10:
    if num > 8:
        break          # Dừng hẳn vòng lặp khi vượt quá 8
    if num % 3 == 0:
        num += 1
        continue       # Bỏ qua các số chia hết cho 3 (không in)
    print("selected:", num)
    num += 1
```

Giải thích:
- Vòng lặp đếm ngược: Mỗi lần in xong phải giảm `remaining -= 1`. Nếu quên dòng này, `remaining` sẽ luôn bằng 5 và vòng lặp sẽ chạy vô tận (lỗi treo chương trình).
- Từ khóa `break`: Lập tức thoát khỏi vòng lặp ngay tại chỗ, bỏ qua toàn bộ các lần lặp còn lại phía sau.
- Từ khóa `continue`: Bỏ qua các dòng lệnh phía dưới của lần lặp này và nhảy ngay sang lần lặp tiếp theo. (Trong code trên, khi gặp số chia hết cho 3, lệnh `continue` bỏ qua lệnh `print` để không in số đó ra).

---

### Bài 3: Tạo danh sách nhanh bằng List Comprehension (ex03_patterns.py)

Code:
```python
numbers = range(1, 11)

# 1. Tạo danh sách bình phương: 1 dòng thay vì 4 dòng
squares = [n**2 for n in numbers]

# 2. Tạo danh sách số chẵn kèm điều kiện lọc (if)
even_numbers = [n for n in numbers if n % 2 == 0]

# 3. Viết theo kiểu thông thường để so sánh độ dài:
evens_loop = []
for n in numbers:
    if n % 2 == 0:
        evens_loop.append(n)

print(squares, even_numbers)
```

Giải thích:
- List Comprehension là "đặc sản" của Python.
- Thay vì phải:
  1. Tạo danh sách rỗng `evens_loop = []`
  2. Viết vòng lặp `for n in numbers:`
  3. Viết điều kiện `if n % 2 == 0:`
  4. Thêm vào danh sách `evens_loop.append(n)`
- Ta gộp tất cả vào trong cặp ngoặc vuông `[...]` đúng 1 dòng: `[n for n in numbers if n % 2 == 0]`. Vừa ngắn hơn rất nhiều, vừa chạy nhanh hơn vì được tối ưu ở tầng ngôn ngữ.

---

### Mini-project: Báo cáo kết quả học tập (mini-project/starter.py)

Code:
```python
topics = ["loops", "enumerate", "zip", "comprehensions"]
scores = [8, 9, 8, 7]

# Duyệt song song có đánh số thứ tự
for position, (topic, score) in enumerate(
    zip(topics, scores, strict=True), start=1
):
    print(f"{position}. {topic}: {score}")

# Lọc các môn đạt điểm giỏi (>= 8) bằng comprehension
strong_scores = [score for score in scores if score >= 8]
print(f"strong_scores={strong_scores}")
```

Giải thích:
- Kết hợp cả `enumerate` và `zip` trong cùng một vòng lặp `for`: Vừa có số thứ tự tự động 1, 2, 3... vừa lấy được cùng lúc tên môn học và điểm số tương ứng.
- Lọc điểm số giỏi chỉ bằng một dòng List Comprehension gọn gàng.

---

## 3. Những lỗi dễ mắc phải nhất trong Tuần 06

1. Vòng lặp vô tận (Infinite Loop) trong `while`:
   - Quên không tăng hoặc giảm biến điều kiện ở trong thân vòng `while` khiến điều kiện luôn đúng và chương trình chạy mãi mãi không dừng, gây đơ máy.
2. Nhầm lẫn phạm vi dừng của `range()`:
   - `range(1, 10)` chỉ chạy từ 1 đến 9, không bao giờ chạm đến số 10. Muốn lấy cả số 10 thì phải viết `range(1, 11)`.
3. Lạm dụng List Comprehension quá phức tạp:
   - Chỉ nên dùng List Comprehension khi công thức ngắn gọn (1 dòng). Nếu có quá nhiều điều kiện `if/else` lồng nhau thì nên viết lại dạng vòng lặp `for` thông thường để người khác đọc code dễ hiểu hơn.
