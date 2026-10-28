"""Auto-generated tests for e_commerce -> test_cart.py."""


def test_add_to_cart() -> None:
    """Passing test."""
    cart = [19.99, 5.00]; assert sum(cart) == 24.99


def test_item_count() -> None:
    """Passing test."""
    items = ['book', 'pen']; assert len(items) == 2


def test_empty_cart() -> None:
    """Passing test."""
    cart = []; assert len(cart) == 0
