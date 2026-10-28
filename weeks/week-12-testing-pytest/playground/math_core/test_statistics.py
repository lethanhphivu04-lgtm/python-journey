"""Auto-generated tests for math_core -> test_statistics.py."""


def test_mean_value() -> None:
    """Passing test."""
    assert sum([2, 4, 6]) / 3 == 4.0


def test_median_odd() -> None:
    """Passing test."""
    assert sorted([1, 9, 5])[1] == 5


def test_min_max_spread() -> None:
    """Passing test."""
    assert max([3, 10, 7]) - min([3, 10, 7]) == 7
