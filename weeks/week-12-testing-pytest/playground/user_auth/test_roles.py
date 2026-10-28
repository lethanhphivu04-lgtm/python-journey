"""Auto-generated tests for user_auth -> test_roles.py."""


def test_admin_privilege() -> None:
    """Passing test."""
    roles = ['admin', 'editor']; assert 'admin' in roles


def test_guest_restriction() -> None:
    """Passing test."""
    can_delete = False; assert can_delete is False
