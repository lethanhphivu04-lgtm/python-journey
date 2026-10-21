# Tổng kết kiến thức Tuần 09: Đồ án Giữa kỳ (Midterm Project)

- Sinh viên: Lê Thanh Phi Vũ
- MSSV: 2123110178
- Môn học: Lập trình Python

---

## 1. Cốt lõi của Midterm Project

- **Mục tiêu:** Không nạp thêm cú pháp mới, mà tổng hợp toàn diện kiến thức từ Tuần 01 đến Tuần 08 thành một sản phẩm hoàn chỉnh, chạy ổn định và có bằng chứng kiểm chứng (**Evidence**).
- **Chu trình phát triển bài bản:**
  $$\text{Learn} \rightarrow \text{Build} \rightarrow \text{Test} \rightarrow \text{Debug} \rightarrow \text{Improve} \rightarrow \text{Commit} \rightarrow \text{Prove}$$
- **Nguyên tắc kỹ thuật:**
  1. **Phân rã hàm (Decomposition):** Chia nhỏ bài toán, mỗi hàm giữ đúng một chức năng.
  2. **Tránh Global State:** Toàn bộ dữ liệu truyền qua tham số và kết quả trả về qua `return`.
  3. **Mô hình hóa dữ liệu:** Sử dụng `dict` và `list` lồng nhau linh hoạt thay vì vội vã tạo Class phức tạp.
  4. **Kiểm thử trường hợp biên (Boundary Cases):** Luôn xử lý danh sách rỗng, chia cho 0, hoặc giá trị thiếu sót.

---

## 2. Chi tiết cả 2 Track và mô tả Code

### Track A: VuaCóc Bot V1 (Heuristic Local Arena)

File: `weeks/week-09-midterm-project/starter/vuacoc_bot_v1.py`

Code:
```python
LOCAL_ACTIONS = {"left", "right", "wait"}


def choose_action(state: dict[str, int]) -> str:
    """Return a deterministic course-local action from 2–4 explainable rules."""
    position = state.get("position", 0)
    goal = state.get("goal", position)
    opponent = state.get("opponent_position")

    if position == goal:
        return "wait"
    if opponent is not None and abs(position - opponent) <= 1:
        return "wait"
    return "right" if position < goal else "left"


def explain_action(state: dict[str, int], action: str) -> str:
    """Explain which observed state values led to an action."""
    pos = state.get("position", "?")
    goal = state.get("goal", "?")
    opp = state.get("opponent_position", "none")
    return f"position={pos}, goal={goal}, opponent={opp} -> action={action}"
```

Giải thích giải thuật:
- **Rule 1 (Đạt mục tiêu):** `position == goal` -> trả `"wait"`.
- **Rule 2 (Phòng thủ / Né va chạm):** Nếu đối thủ ở sát bên cạnh ($|\text{position} - \text{opponent}| \le 1$) -> trả `"wait"`.
- **Rule 3 (Tiến tới đích):** Nếu đang ở bên trái đích (`position < goal`) -> đi `"right"`, ngược lại đi `"left"`.
- **Kết quả đấu thử trên Local Arena (`reference/evaluate_baselines.py`):**
  - Đấu với `WaitBot`: Kết thúc hoàn tất sau 6 lượt (Hòa).
  - Đấu với `ForwardBot`: Kết thúc hoàn tất sau 4 lượt.
  - Đấu với `CautiousBot`: Kết thúc hoàn tất sau 6 lượt (Hòa).
  - Luôn trả về action hợp lệ trong tập `LOCAL_ACTIONS`, không bao giờ vi phạm luật chơi.

---

### Track B: Quản lý học sinh (Student Manager)

File: `weeks/week-09-midterm-project/starter/student_manager.py`

Code:
```python
def calculate_average(student: dict[str, object]) -> float:
    """Tính điểm trung bình từ danh sách điểm của học sinh."""
    scores = student.get("scores", [])
    if not isinstance(scores, list) or not scores:
        return 0.0
    return sum(float(s) for s in scores) / len(scores)


def classify_student(average: float) -> str:
    """Xếp loại học lực theo điểm trung bình."""
    if average >= 8.0:
        return "Giỏi"
    if average >= 6.5:
        return "Khá"
    if average >= 5.0:
        return "Đạt"
    return "Cần cố gắng"


def find_student(
    students: list[dict[str, object]], query: str
) -> dict[str, object] | None:
    """Tìm kiếm học sinh theo tên không phân biệt hoa thường."""
    q = query.strip().lower()
    for student in students:
        if str(student.get("name", "")).strip().lower() == q:
            return student
    return None


def generate_report(students: list[dict[str, object]]) -> str:
    """Tạo báo cáo tổng kết toàn bộ lớp học."""
    if not students:
        return "Danh sách rỗng"
    lines = []
    total_avg = 0.0
    for student in students:
        avg = calculate_average(student)
        total_avg += avg
        lines.append(f"- {student.get('name', '?')}: {avg:.1f} [{classify_student(avg)}]")
    class_avg = total_avg / len(students)
    lines.append(f"Điểm trung bình cả lớp: {class_avg:.2f}")
    return "\n".join(lines)
```

Giải thích giải thuật:
- **Cấu trúc dữ liệu:** Danh sách lồng nhau `list[dict]` giúp dễ dàng duyệt qua và thêm/bớt học sinh.
- **`calculate_average`:** Xử lý triệt để trường hợp học sinh chưa có điểm hoặc danh sách rỗng (trả về `0.0`, tránh `ZeroDivisionError`).
- **`find_student`:** Chuẩn hóa chuỗi bằng `.strip().lower()` giúp tìm kiếm chính xác kể cả khi người dùng nhập khoảng trắng thừa hoặc viết hoa.
- **`generate_report`:** Kết hợp các hàm thành phần để tính điểm trung bình cả lớp và xuất bảng tổng kết định dạng rõ ràng.

---

## 3. Những lỗi dễ mắc phải và bài học kinh nghiệm

1. **Lỗi chia cho 0 (`ZeroDivisionError`):**
   - Rất dễ xảy ra khi danh sách điểm `scores` là danh sách rỗng `[]` hoặc danh sách lớp `students` rỗng. Luôn cần guard clause kiểm tra độ dài trước khi thực hiện phép chia.
2. **Lạm dụng biến toàn cục (`global`):**
   - Viết các hàm tự ý đọc biến danh sách ở ngoài thay vì truyền qua parameter. Khi viết test hoặc chạy với nhiều danh sách khác nhau sẽ gây xung đột dữ liệu.
3. **Ảo tưởng về tỷ lệ thắng (Track Bot):**
   - Nghĩ rằng bot phải thắng 100% mới đạt. Mục tiêu của Midterm là bot chạy đúng luật, giải thích được quy tắc đưa ra quyết định, và nhận diện được điểm yếu để nâng cấp ở các tuần sau.
