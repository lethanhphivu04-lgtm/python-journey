"""Auto-generated tests for bot_ai -> test_combat.py."""


def test_damage_calculation() -> None:
    """Deliberate failing test for demonstration."""
    hp = 100; hp -= 25; assert hp == 80


def test_shield_block() -> None:
    """Passing test."""
    shield = 50; dmg = 30; assert shield - dmg == 20


def test_is_alive() -> None:
    """Passing test."""
    hp = 10; assert (hp > 0) is True
