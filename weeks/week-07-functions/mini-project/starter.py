"""Starter for the Week 07 Personal Utility Toolkit."""


def calculate_subtotal(price: float, quantity: int) -> float:
    """Return price multiplied by quantity."""
    if quantity <= 0:
        return 0.0
    return price * quantity


def calculate_discount(subtotal: float, percent: float = 0) -> float:
    """Return the discount amount, not the final total."""
    return subtotal * percent / 100


def calculate_average(scores: list[float]) -> float:
    """Return the average, or 0 for an empty list."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def classify_score(average: float) -> str:
    """Return a short classification for an average score."""
    if average >= 8.0:
        return "Giỏi"
    if average >= 5.0:
        return "Đạt"
    return "Cần luyện thêm"


def format_currency(amount: float) -> str:
    """Return an amount formatted in đồng."""
    return f"{amount:,.0f} đ"


def main() -> None:
    """Compose the toolkit functions into a visible program flow."""
    price, quantity, discount_pct = 50_000, 3, 10
    subtotal = calculate_subtotal(price, quantity)
    discount = calculate_discount(subtotal, discount_pct)
    total = subtotal - discount
    print(f"Hóa đơn: {format_currency(total)} (gốc {format_currency(subtotal)}, giảm {format_currency(discount)})")

    scores = [8.5, 9.0, 7.5]
    avg = calculate_average(scores)
    print(f"Điểm TB: {avg:.2f} -> Xếp loại: {classify_score(avg)}")


if __name__ == "__main__":
    main()
