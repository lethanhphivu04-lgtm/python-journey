"""Auto-generated tests for network_api -> test_http_status.py."""


def test_get_ok() -> None:
    """Deliberate failing test for demonstration."""
    status = 404; assert status == 200


def test_created() -> None:
    """Passing test."""
    status = 201; assert status == 201


def test_not_found() -> None:
    """Deliberate failing test for demonstration."""
    status = 200; assert status == 404
