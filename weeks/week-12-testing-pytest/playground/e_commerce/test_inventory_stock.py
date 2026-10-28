"""Auto-generated tests for e_commerce -> test_inventory_stock.py."""


def test_stock_decreased() -> None:
    """Passing test."""
    stock = 10; stock -= 1; assert stock == 9


def test_out_of_stock_flag() -> None:
    """Deliberate failing test for demonstration."""
    stock = 5; assert stock <= 0
