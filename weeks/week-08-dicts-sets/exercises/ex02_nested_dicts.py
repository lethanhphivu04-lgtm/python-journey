"""Exercise 02: đọc và biến đổi nested data."""


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


def main() -> None:
    """Chạy starter với một classroom nhỏ."""
    classroom = {
        "An": {"age": 20, "scores": [8, 9, 7]},
        "Bình": {"age": 21, "scores": [7, 6, 8]},
    }
    print(hoc_sinh_tot_nhat(classroom))


if __name__ == "__main__":
    main()
