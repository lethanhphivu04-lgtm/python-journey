"""Exercise 03 — Local scope and avoiding unnecessary global state.

Goal:
    Truyền dữ liệu qua parameter thay vì để hàm phụ thuộc vào biến global.

TODO:
    1. Hoàn thành ``them_ghi_chu``.
    2. Hoàn thành ``tim_ghi_chu``.
    3. Hoàn thành ``dem_ghi_chu``.

Examples:
    notes = []
    them_ghi_chu(notes, "Học return")
    dem_ghi_chu(notes) == 1

Expected behavior:
    Các hàm chỉ dùng list được caller truyền vào; không tạo global notebook.

Basic invalid case:
    Ghi chú chỉ chứa khoảng trắng không được thêm vào list.

Self-check command:
    python weeks/week-07-functions/exercises/ex03_scope.py
"""


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


if __name__ == "__main__":
    notes: list[str] = []
    print("Thêm hợp lệ:", them_ghi_chu(notes, " Học return "))
    print("Thêm rỗng:", them_ghi_chu(notes, "   "))
    them_ghi_chu(notes, "Luyện scope")
    print("Tìm 'return':", tim_ghi_chu(notes, "RETURN"))
    print("Tổng số ghi chú:", dem_ghi_chu(notes))
