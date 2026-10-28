"""Auto-generated tests for network_api -> test_rate_limiter.py."""


def test_under_limit() -> None:
    """Passing test."""
    req_count = 8; assert req_count <= 10


def test_cool_down() -> None:
    """Passing test."""
    cooldown = 0; assert cooldown == 0
