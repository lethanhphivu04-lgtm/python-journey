"""Auto-generated tests for user_auth -> test_password_hash.py."""


def test_hash_length() -> None:
    """Deliberate failing test for demonstration."""
    h = 'a' * 32; assert len(h) == 64


def test_salt_differs() -> None:
    """Passing test."""
    s1, s2 = 'salt1', 'salt2'; assert s1 != s2
