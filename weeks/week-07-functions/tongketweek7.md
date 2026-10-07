# Tổng kết kiến thức Tuần 07: Hàm, Phạm vi biến (Scope) và Phân rã bài toán

- Sinh viên: Lê Thanh Phi Vũ
- MSSV: 2123110178
- Môn học: Lập trình Python

---

## 1. Cốt lõi về Hàm (Functions) trong Python

- **Hàm là gì?** Là một khối lệnh được đóng gói lại, có tên rõ nghĩa, giúp tái sử dụng mã nguồn và chia nhỏ bài toán phức tạp thành nhiều phần dễ quản lý (**Decomposition**).
- **`return` khác `print` như thế nào?**
  - `print()` chỉ hiển thị kết quả ra màn hình cho người dùng xem, giá trị sau đó biến mất.
  - `return` trả lại giá trị tính toán cho nơi gọi hàm, cho phép kết quả được dùng làm đầu vào cho các bước xử lý tiếp theo.
- **Phạm vi biến (Scope):** Biến khai báo bên trong hàm là biến cục bộ (Local Scope), chỉ tồn tại khi hàm thực thi và biến mất khi hàm kết thúc. Hạn chế tối đa việc lạm dụng biến toàn cục (`global`).
- **Type hints:** Giúp người đọc và trình soạn thảo hiểu kiểu dữ liệu mong đợi (`def func(a: int) -> str:`), nhưng Python không tự động validate kiểu dữ liệu lúc runtime.

---

## 2. Chi tiết bài tập, giải thuật và mô tả code

### Bài 1: Hàm cơ bản và giá trị trả về (ex01_basic_func.py)

Code:
```python
import math


def chao(ten: str) -> str:
    """Trả về lời chào cho ten."""
    return f"Xin chào {ten}!"


def tinh_dien_tich_hinh_tron(ban_kinh: float) -> float:
    """Trả về diện tích hình tròn."""
    return math.pi * ban_kinh**2


def la_so_chan(so: int) -> bool:
    """Trả về True khi so là số chẵn."""
    return so % 2 == 0
```

Giải thích:
- Dùng `return` ở mọi hàm để caller có thể tiếp tục tính toán hoặc định dạng.
- `tinh_dien_tich_hinh_tron`: Dùng hằng số `math.pi` từ thư viện chuẩn và toán tử lũy thừa `** 2`. Với bán kính bằng 0, hàm trả về đúng `0.0` (boundary case).
- `la_so_chan`: Dùng phép chia lấy dư `% 2 == 0` để trả về trực tiếp giá trị boolean (`True`/`False`), không cần bọc trong `if/else` rườm rà.

---

### Bài 2: Tham số mặc định và Phân rã luồng tính toán (ex02_params.py)

Code:
```python
def gioi_thieu(ten: str, tuoi: int = 18) -> str:
    """Trả về một câu giới thiệu ngắn."""
    return f"Tôi là {ten}, {tuoi} tuổi."


def tinh_tam_tinh(gia: float, so_luong: int) -> float:
    """Tính tạm tính; trả về 0 nếu số lượng không dương."""
    if so_luong <= 0:
        return 0.0
    return gia * so_luong


def ap_dung_giam_gia(tam_tinh: float, phan_tram: float = 0) -> float:
    """Trả về số tiền sau giảm giá."""
    return tam_tinh - (tam_tinh * phan_tram / 100)


def tao_hoa_don(gia: float, so_luong: int, phan_tram: float = 0) -> str:
    """Ghép các bước nhỏ và trả về dòng tổng tiền."""
    tam_tinh = tinh_tam_tinh(gia, so_luong)
    tong = ap_dung_giam_gia(tam_tinh, phan_tram)
    return f"Tổng: {tong:,.0f} đ"
```

Giải thích:
- `tuoi: int = 18`: Tham số mặc định (default parameter). Nếu caller không truyền `tuoi`, hàm sẽ tự lấy 18.
- Boundary check trong `tinh_tam_tinh`: Nếu `so_luong <= 0`, trả về ngay `0.0` thay vì tính ra giá trị âm không hợp lệ.
- Phân rã bài toán: Hàm `tao_hoa_don` không tự tính toán toàn bộ từ đầu đến cuối mà gọi lại hai hàm con `tinh_tam_tinh` và `ap_dung_giam_gia`. Mỗi hàm giữ một trách nhiệm duy nhất (Single Responsibility).

---

### Bài 3: Phạm vi biến cục bộ, tránh phụ thuộc Global State (ex03_scope.py)

Code:
```python
def them_ghi_chu(danh_sach: list[str], noi_dung: str) -> bool:
    """Thêm ghi chú hợp lệ và báo thao tác có thành công hay không."""
    ghi_chu = noi_dung.strip()
    if not ghi_chu:
        return False
    danh_sach.append(ghi_chu)
    return True


def tim_ghi_chu(danh_sach: list[str], tu_khoa: str) -> list[str]:
    """Trả về các ghi chú chứa từ khóa, không phân biệt hoa thường."""
    tu_khoa_thuong = tu_khoa.lower()
    return [g for g in danh_sach if tu_khoa_thuong in g.lower()]


def dem_ghi_chu(danh_sach: list[str]) -> int:
    """Trả về số ghi chú trong list được truyền vào."""
    return len(danh_sach)
```

Giải thích:
- Toàn bộ dữ liệu sổ tay được lưu trong `danh_sach` do người gọi truyền vào qua tham số. Hàm không tự ý tạo hay sửa biến global ở ngoài module.
- `noi_dung.strip()`: Loại bỏ khoảng trắng thừa hai đầu và kiểm tra nếu rỗng thì trả về `False` (bảo vệ tính toàn vẹn của dữ liệu).
- `tu_khoa.lower()` & `g.lower()`: Chuyển chuỗi về chữ thường trước khi so sánh giúp tìm kiếm không phân biệt hoa thường (case-insensitive).

---

### Bài 4: Hàm ra quyết định tất định (ex04_decision_function.py)

Code:
```python
def choose_action(state: str) -> str:
    """Return a deterministic teaching action for state."""
    if state == "danger":
        return "defend"
    if state == "opportunity":
        return "advance"
    return "wait"
```

Giải thích:
- Tính tất định (deterministic): Cùng một trạng thái đầu vào luôn luôn trả về cùng một hành động đầu ra.
- Trả về fallback `"wait"` cho mọi trạng thái bất thường (chuỗi rỗng, giá trị lạ), đảm bảo hàm an toàn và không bao giờ crash.

---

### Mini-project: Bộ công cụ tiện ích cá nhân (mini-project/starter.py)

Code:
```python
def calculate_subtotal(price: float, quantity: int) -> float:
    """Tính tạm tính; trả về 0 khi số lượng không dương."""
    if quantity <= 0:
        return 0.0
    return price * quantity


def calculate_discount(subtotal: float, percent: float = 0) -> float:
    """Tính tiền giảm theo phần trăm."""
    return subtotal * percent / 100


def calculate_average(scores: list[float]) -> float:
    """Tính trung bình danh sách điểm; trả về 0 nếu danh sách rỗng."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def classify_score(average: float) -> str:
    """Phân loại học lực theo điểm trung bình."""
    if average >= 8.0:
        return "Giỏi"
    if average >= 5.0:
        return "Đạt"
    return "Cần luyện thêm"


def format_currency(amount: float) -> str:
    """Định dạng tiền tệ theo chuẩn Việt Nam."""
    return f"{amount:,.0f} đ"


def main() -> None:
    """Ghép các hàm thành luồng xử lý hoàn chỉnh."""
    price, quantity, discount_pct = 50_000, 3, 10
    subtotal = calculate_subtotal(price, quantity)
    discount = calculate_discount(subtotal, discount_pct)
    total = subtotal - discount
    print(f"Hóa đơn: {format_currency(total)} (gốc {format_currency(subtotal)}, giảm {format_currency(discount)})")

    scores = [8.5, 9.0, 7.5]
    avg = calculate_average(scores)
    print(f"Điểm TB: {avg:.2f} -> Xếp loại: {classify_score(avg)}")
```

Giải thích:
- Chuỗi xử lý hóa đơn: `price + quantity` -> `subtotal` -> `discount` -> `total` -> `format_currency`. Mỗi hàm chỉ nhận input cần thiết và trả output rõ ràng.
- Chuỗi đánh giá điểm: `scores` -> `calculate_average` -> `classify_score`.

---

## 3. Những lỗi dễ mắc phải nhất trong Tuần 07

1. **Nhầm lẫn giữa `print()` và `return`:**
   - Khi viết hàm chỉ có `print()` mà quên `return`, Python sẽ tự gán giá trị trả về là `None`. Khi lấy kết quả hàm đó gán cho biến khác hoặc đem đi cộng trừ sẽ gặp lỗi `TypeError: unsupported operand type...`.
2. **Khai báo tham số mặc định sai thứ tự:**
   - Trong Python, tất cả các tham số bắt buộc phải đứng trước tham số có giá trị mặc định. Viết `def tinh(a=10, b):` sẽ báo lỗi ngay lập tức (`SyntaxError: non-default argument follows default argument`).
3. **Hiểu lầm về Type Hints:**
   - Nghĩ rằng ghi `so: int` thì người dùng truyền chuỗi vào Python sẽ tự chặn. Type hints chỉ là thông tin gợi ý cho lập trình viên và IDE; muốn chặn dữ liệu sai ở runtime thì bắt buộc phải viết mã kiểm tra (`if not isinstance(...)` hoặc validation).
