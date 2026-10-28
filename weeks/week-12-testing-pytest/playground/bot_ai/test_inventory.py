"""Auto-generated tests for bot_ai -> test_inventory.py."""


def test_bag_capacity() -> None:
    """Deliberate failing test for demonstration."""
    bag = ['potion', 'sword']; assert len(bag) == 3


def test_has_key() -> None:
    """Passing test."""
    items = {'bronze_key', 'shield'}; assert 'bronze_key' in items


def test_gold_coins() -> None:
    """Passing test."""
    gold = 150; gold += 50; assert gold == 200
