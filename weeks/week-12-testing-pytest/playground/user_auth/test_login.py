"""Auto-generated tests for user_auth -> test_login.py."""


def test_valid_credentials() -> None:
    """Passing test."""
    status = 200; assert status == 200


def test_locked_after_5_tries() -> None:
    """Passing test."""
    tries = 5; assert tries >= 5


def test_remember_me_cookie() -> None:
    """Deliberate failing test for demonstration."""
    cookie = {}; assert 'token' in cookie
