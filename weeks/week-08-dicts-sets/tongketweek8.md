# Tổng kết kiến thức Tuần 08: Từ điển (Dictionary), Tập hợp (Set) và Mô hình hóa dữ liệu

- Sinh viên: Lê Thanh Phi Vũ
- MSSV: 2123110178
- Môn học: Lập trình Python

---

## 1. Cốt lõi về Dictionary và Set trong Python

| Tiêu chí | Dictionary (`dict`) | Set (`set`) |
|:---|:---|:---|
| **Cấu trúc** | Cặp khóa - giá trị: `{"tên": "An", "tuổi": 20}` | Tập hợp các phần tử đơn lẻ: `{"Toán", "Văn"}` |
| **Tính duy nhất** | Các **Key** là duy nhất, không được trùng lặp. | Mọi **phần tử** là duy nhất, tự động lọc trùng. |
| **Tốc độ tra cứu** | Cực nhanh: $O(1)$ nhờ bảng băm (hash table). | Cực nhanh: $O(1)$ khi kiểm tra tồn tại (`in`). |
| **Khi nào nên dùng?** | Khi cần ánh xạ thông tin, mô hình hóa thực thể (học sinh, sản phẩm, cấu hình). | Khi cần loại bỏ phần tử trùng lặp hoặc thực hiện các phép toán tập hợp (giao, hợp, hiệu). |

- **Mô hình hóa dữ liệu (Data Modeling):** Trước khi nghĩ đến việc tạo Class phức tạp, kết hợp lồng nhau giữa `dict`, `list` và `set` là cách đơn giản và linh hoạt nhất để biểu diễn trạng thái của hệ thống.

---

## 2. Chi tiết bài tập, giải thuật và mô tả code

### Bài 1: Thao tác cơ bản trên Dictionary (ex01_dicts.py)

Code:
```python
def cap_nhat_diem(
    scores: dict[str, float], subject: str, score: float
) -> dict[str, float]:
    """Trả một dict mới có điểm được thêm hoặc cập nhật."""
    updated = scores.copy()
    updated[subject] = score
    return updated


def diem_trung_binh(scores: dict[str, float]) -> float:
    """Trả điểm trung bình, hoặc 0.0 nếu dict rỗng."""
    if not scores:
        return 0.0
    return sum(scores.values()) / len(scores)


def dem_tan_suat(text: str) -> dict[str, int]:
    """Đếm tần suất ký tự, bỏ qua khoảng trắng."""
    frequency: dict[str, int] = {}
    for character in text:
        if not character.isspace():
            frequency[character] = frequency.get(character, 0) + 1
    return frequency
```

Giải thích:
- `scores.copy()`: Tránh thay đổi trực tiếp dict ban đầu (tránh side-effect), trả về bản sao an toàn cho caller.
- `scores.values()`: Lấy ra toàn bộ danh sách điểm số để tính tổng bằng `sum()` và chia cho số môn `len(scores)`.
- `frequency.get(character, 0)`: Phương thức `.get()` thần thánh giúp đọc giá trị an toàn. Nếu ký tự chưa có trong dict, nó tự trả về `0` thay vì báo lỗi `KeyError`.

---

### Bài 2: Đọc và biến đổi dữ liệu lồng nhau (ex02_nested_dicts.py)

Code:
```python
def diem_trung_binh(student: dict[str, object]) -> float:
    """Tính trung bình list scores trong một student model."""
    scores = student.get("scores", [])
    if not isinstance(scores, list) or not scores:
        return 0.0
    return sum(scores) / len(scores)


def hoc_sinh_tot_nhat(classroom: dict[str, dict[str, object]]) -> str:
    """Trả tên learner có điểm trung bình cao nhất."""
    best_name = ""
    best_average = -1.0
    for name, student in classroom.items():
        average = diem_trung_binh(student)
        if average > best_average:
            best_name = name
            best_average = average
    return best_name


def tong_gia_tri_kho(products: dict[str, dict[str, object]]) -> float:
    """Tính tổng price nhân quantity của mọi product."""
    total = 0.0
    for product in products.values():
        price = product.get("price", 0)
        quantity = product.get("quantity", 0)
        total += float(price) * int(quantity)
    return total
```

Giải thích:
- Dữ liệu lồng nhau: Mỗi giá trị của `classroom` lại là một `dict` chứa thông tin chi tiết (tuổi, danh sách điểm).
- Tái sử dụng hàm: `hoc_sinh_tot_nhat` gọi lại hàm con `diem_trung_binh(student)` cho từng học sinh để so sánh tìm người có điểm cao nhất.
- Tính toán tổng kho: Duyệt qua từng sản phẩm qua `products.values()`, lấy an toàn `price` và `quantity` rồi nhân lại cộng dồn.

---

### Bài 3: Tập hợp Set và các phép toán tập hợp (ex03_sets.py)

Code:
```python
def phan_tich_mon_hoc(
    semester_one: set[str], semester_two: set[str]
) -> dict[str, set[str]]:
    """Trả các nhóm common, only_one, only_two và all."""
    return {
        "common": semester_one & semester_two,
        "only_one": semester_one - semester_two,
        "only_two": semester_two - semester_one,
        "all": semester_one | semester_two,
    }


def loai_trung_giu_thu_tu(words: list[str]) -> list[str]:
    """Loại từ trùng nhưng giữ thứ tự xuất hiện đầu tiên."""
    seen: set[str] = set()
    unique: list[str] = []
    for word in words:
        if word not in seen:
            seen.add(word)
            unique.append(word)
    return unique


def tu_chung(first: str, second: str) -> set[str]:
    """Trả các từ lowercase xuất hiện trong cả hai câu."""
    return set(first.lower().split()) & set(second.lower().split())


def la_anagram(first: str, second: str) -> bool:
    """Kiểm tra hai chuỗi có cùng ký tự và số lần xuất hiện."""
    return sorted(first.lower().replace(" ", "")) == sorted(
        second.lower().replace(" ", "")
    )
```

Giải thích:
- Các phép toán trên Set:
  - `&` (Intersection): Lấy phần giao (các môn học cả hai kỳ).
  - `-` (Difference): Lấy phần hiệu (các môn chỉ học ở một kỳ).
  - `|` (Union): Lấy phần hợp (tất cả các môn của cả hai kỳ).
- `loai_trung_giu_thu_tu`: Sử dụng `seen` dạng Set để kiểm tra `word not in seen` trong $O(1)$, kết hợp `unique` dạng List để giữ nguyên thứ tự ban đầu.

---

### Bài 4: Heuristic ra quyết định từ trạng thái có cấu trúc (ex04_bot_state_heuristic.py)

Code:
```python
LOCAL_ACTIONS = {"left", "right", "wait"}


def choose_action(state: dict[str, int]) -> str:
    """Chọn một action local bằng 2–4 rules dễ giải thích."""
    position = state.get("position", 0)
    goal = state.get("goal", position)
    opponent = state.get("opponent_position")

    if position == goal:
        return "wait"
    if opponent is not None and abs(position - opponent) <= 1:
        return "wait"
    if position < goal:
        return "right"
    return "left"
```

Giải thích:
- Dùng `state.get()` để đọc linh hoạt cả field bắt buộc lẫn optional (`opponent_position`).
- Các quy tắc ra quyết định đơn giản, dễ giải thích:
  1. Đã tới đích -> `"wait"`.
  2. Đối thủ quá gần (khoảng cách <= 1) -> `"wait"` phòng thủ.
  3. Ở bên trái đích -> đi `"right"`.
  4. Ở bên phải đích -> đi `"left"`.

---

### Mini-project: Dashboard ra quyết định (mini-project/starter.py)

Code:
```python
REQUIRED_FIELDS = {"position", "goal"}
LOCAL_ACTIONS = {"left", "right", "wait"}


def validate_state(state: dict[str, object]) -> bool:
    """Kiểm tra xem tất cả các field bắt buộc có tồn tại không."""
    return REQUIRED_FIELDS.issubset(state.keys())


def summarize_state(state: dict[str, object]) -> str:
    """Tạo tóm tắt ngắn gọn trạng thái hiện tại."""
    pos = state.get("position", "?")
    goal = state.get("goal", "?")
    opp = state.get("opponent_position", "không có")
    return f"Vị trí: {pos} | Mục tiêu: {goal} | Đối thủ: {opp}"


def recommend_action(state: dict[str, object]) -> str:
    """Đưa ra đề xuất hành động dựa trên quy tắc có thể giải thích."""
    if not validate_state(state):
        return "wait"
    pos = int(state["position"])
    goal = int(state["goal"])
    opp = state.get("opponent_position")

    if pos == goal:
        return "wait"
    if opp is not None and abs(pos - int(opp)) <= 1:
        return "wait"
    return "right" if pos < goal else "left"


def main() -> None:
    dashboard = {
        "state": {
            "position": 1,
            "opponent_position": 3,
            "goal": 4,
        },
        "tags": {"course-local", "week-08"},
    }
    state = dashboard["state"]
    print("valid=", validate_state(state))
    print(summarize_state(state))
    print("action=", recommend_action(state))
```

Giải thích:
- `REQUIRED_FIELDS.issubset(state.keys())`: Sử dụng phương thức tập hợp `issubset` để kiểm tra toàn bộ các field bắt buộc chỉ trong 1 dòng.
- Phân biệt rõ ràng giữa required field (`position`, `goal`) và optional field (`opponent_position`).

---

## 3. Những lỗi dễ mắc phải nhất trong Tuần 08

1. **Gặp lỗi `KeyError` khi truy cập trực tiếp bằng ngoặc vuông:**
   - Dùng `data["not_exist"]` sẽ làm crash chương trình nếu key chưa có. Luôn ưu tiên dùng `data.get("not_exist", default_value)` khi key có thể không xuất hiện.
2. **Khởi tạo nhầm Set rỗng:**
   - Viết `s = {}` thực chất là tạo một **Dictionary rỗng**, không phải Set. Muốn tạo Set rỗng bắt buộc phải dùng `s = set()`.
3. **Thay đổi trực tiếp Dict khi chưa sao chép (`.copy()`):**
   - Khi truyền một dict vào hàm và thực hiện gán `d["key"] = val`, dict ở bên ngoài hàm cũng bị thay đổi theo (vì dict là mutable). Khi muốn tạo dict mới mà không ảnh hưởng dữ liệu cũ, hãy gọi `.copy()` trước.
