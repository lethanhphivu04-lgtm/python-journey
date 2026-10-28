"""Unit tests for Vua Cóc Web Application backend logic."""

from app import (
    ACTIONS_2D,
    BOT_REGISTRY,
    create_2d_game,
    smart_2d_ai,
)


def test_create_2d_game_structure() -> None:
    """A fresh 2D game state contains valid grid, frogs, obstacles, and flies."""
    game = create_2d_game(grid_size=5, num_rocks=3, num_flies=3)

    assert game["grid_size"] == 5
    assert game["max_turns"] == 15
    assert game["current_turn"] == 1
    assert game["frog_a"]["x"] == 0
    assert game["frog_a"]["y"] == 0
    assert game["frog_b"]["x"] == 4
    assert game["frog_b"]["y"] == 4
    assert len(game["rocks"]) == 3
    assert len(game["flies"]) == 3
    assert game["is_finished"] is False
    assert game["winner"] is None


def test_create_2d_game_custom_parameters() -> None:
    """create_2d_game respects custom grid sizes and obstacle counts."""
    game = create_2d_game(grid_size=7, num_rocks=4, num_flies=5)

    assert game["grid_size"] == 7
    assert len(game["rocks"]) == 4
    assert len(game["flies"]) == 5
    assert game["frog_b"]["x"] == 6
    assert game["frog_b"]["y"] == 6


def test_smart_2d_ai_returns_valid_action_and_thought() -> None:
    """smart_2d_ai returns a tuple of (action, thought) with a legal 2D action."""
    game = create_2d_game()
    action_b, thought_b = smart_2d_ai("b", game)

    assert action_b in ACTIONS_2D
    assert isinstance(thought_b, str)
    assert len(thought_b) > 0


def test_smart_2d_ai_avoids_rocks() -> None:
    """smart_2d_ai never steps into an adjacent rock cell."""
    game = {
        "grid_size": 3,
        "max_turns": 10,
        "current_turn": 1,
        "frog_a": {"x": 0, "y": 0, "goal": {"x": 2, "y": 2}, "score": 0},
        "frog_b": {"x": 2, "y": 2, "goal": {"x": 0, "y": 0}, "score": 0},
        "rocks": [{"x": 1, "y": 2}],  # Rock to the left of B (2, 2)
        "flies": [],
        "is_finished": False,
        "winner": None,
        "reason": "",
    }
    action_b, _ = smart_2d_ai("b", game)
    # B at (2, 2) wanting to go to (0, 0): left is blocked by rock at (1, 2), so should choose up
    assert action_b != "left"
    assert action_b in {"up", "wait"}


def test_smart_2d_ai_for_frog_a() -> None:
    """smart_2d_ai also functions correctly for frog A."""
    game = create_2d_game()
    action_a, thought_a = smart_2d_ai("a", game)

    assert action_a in ACTIONS_2D
    assert isinstance(thought_a, str)


def test_bot_registry_contains_student_bot() -> None:
    """The bot registry includes the student bot along with the baselines."""
    assert "student" in BOT_REGISTRY
    assert "wait" in BOT_REGISTRY
    assert "forward" in BOT_REGISTRY
    assert "cautious" in BOT_REGISTRY
    assert callable(BOT_REGISTRY["student"]["fn"])
