"""Auto-generated tests for bot_ai -> test_navigation.py."""


def test_move_forward() -> None:
    """Deliberate failing test for demonstration."""
    pos = 0; pos += 1; assert pos == 2


def test_boundary_limit() -> None:
    """Passing test."""
    pos = 100; assert min(pos + 10, 100) == 100


def test_turn_around() -> None:
    """Passing test."""
    direction = 'N'; assert {'N': 'S'}[direction] == 'S'
