"""Comprehensive test suite for Student Bot in Vua Cóc Line Arena.

Covers normal, edge, invalid, regression, and contract legality cases
following the Arrange -> Act -> Assert pattern.
"""

import pytest
from student_bot.bot import (
    LOCAL_ACTIONS,
    assess_tactical_situation,
    choose_action,
    explain_decision,
    get_direction_to_goal,
    is_at_goal,
    validate_state,
)

# ==============================================================================
# 1. NORMAL CASES
# ==============================================================================


def test_normal_case_seat_a_moves_right() -> None:
    """Seat A starting at 0 with goal 4 must step right."""
    # Arrange
    state = {"position": 0, "goal": 4, "opponent_position": 4}

    # Act
    action = choose_action(state)

    # Assert
    assert action == "right"
    assert action in LOCAL_ACTIONS


def test_normal_case_seat_b_moves_left() -> None:
    """Seat B starting at 4 with goal 0 must step left."""
    # Arrange
    state = {"position": 4, "goal": 0, "opponent_position": 0}

    # Act
    action = choose_action(state)

    # Assert
    assert action == "left"
    assert action in LOCAL_ACTIONS


def test_helpers_goal_and_direction() -> None:
    """Helper functions correctly report goal arrival and directional step."""
    assert is_at_goal(4, 4) is True
    assert is_at_goal(2, 4) is False
    assert get_direction_to_goal(1, 4) == "right"
    assert get_direction_to_goal(3, 1) == "left"
    assert get_direction_to_goal(2, 2) == "wait"


# ==============================================================================
# 2. BOUNDARY & EDGE CASES
# ==============================================================================


def test_edge_case_already_at_goal_waits() -> None:
    """When the bot has reached the goal, it must wait to preserve its win."""
    # Arrange
    state = {"position": 4, "goal": 4, "opponent_position": 2}

    # Act
    action = choose_action(state)

    # Assert
    assert action == "wait"


def test_edge_case_missing_opponent_continues_to_goal() -> None:
    """If opponent position is None or absent, bot still progresses to goal."""
    # Arrange
    state = {"position": 1, "goal": 4}

    # Act
    action = choose_action(state)

    # Assert
    assert action == "right"


def test_edge_case_final_step_into_goal() -> None:
    """When 1 step away from goal, bot steps directly into the goal."""
    # Arrange (pos=3, goal=4)
    state = {"position": 3, "goal": 4, "opponent_position": 1}

    # Act
    action = choose_action(state)

    # Assert
    assert action == "right"


# ==============================================================================
# 3. DEFENSIVE & INVALID INPUT CASES
# ==============================================================================


def test_invalid_input_none_or_empty_state_falls_back_safely() -> None:
    """Non-dict or empty state must gracefully return 'wait' without raising an unhandled exception."""
    # Act & Assert
    assert choose_action({}) == "wait"
    assert choose_action(None) == "wait"  # type: ignore[arg-type]


def test_invalid_input_wrong_types_falls_back_safely() -> None:
    """Non-integer position or goal must gracefully return 'wait'."""
    # Arrange
    corrupted_state = {"position": "zero", "goal": "four"}  # type: ignore[dict-item]

    # Act & Assert
    assert choose_action(corrupted_state) == "wait"


def test_validate_state_helper() -> None:
    """validate_state correctly identifies valid vs invalid state shapes."""
    assert validate_state({"position": 2, "goal": 4}) is True
    assert validate_state({"position": 2}) is False  # missing goal
    assert validate_state(None) is False
    assert validate_state("invalid") is False  # type: ignore[arg-type]


# ==============================================================================
# 4. REGRESSION CASES
# ==============================================================================


def test_regression_starter_never_freezes_when_goal_is_ahead() -> None:
    """Regression: Early starter code returned 'wait' indefinitely instead of advancing."""
    # Arrange
    state = {"position": 2, "goal": 4, "opponent_position": 3}

    # Act
    action = choose_action(state)

    # Assert: Must NOT freeze with 'wait' when goal is ahead
    assert action != "wait"
    assert action == "right"


def test_regression_goal_behind_moves_left_not_right() -> None:
    """Regression: Earlier simple bots always returned 'right' regardless of direction."""
    # Arrange
    state = {"position": 3, "goal": 1, "opponent_position": 0}

    # Act
    action = choose_action(state)

    # Assert
    assert action == "left"


# ==============================================================================
# 5. EXPLAINABILITY & CONTRACT INTEGRITY
# ==============================================================================


def test_explain_decision_matches_action() -> None:
    """The explanation string must clearly state the chosen action and metrics."""
    # Arrange
    state = {"position": 1, "goal": 4, "opponent_position": 3}

    # Act
    action = choose_action(state)
    explanation = explain_decision(state, action)

    # Assert
    assert "right" in explanation
    assert "dist=3" in explanation


def test_tactical_assessment_metrics() -> None:
    """assess_tactical_situation computes correct mathematical distances."""
    state = {"position": 1, "goal": 4, "opponent_position": 3}
    tactics = assess_tactical_situation(state)

    assert tactics["dist_to_goal"] == 3
    assert tactics["dist_to_opp"] == 2
    assert tactics["step_direction"] == "right"


@pytest.mark.parametrize("pos, goal", [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (4, 0), (2, 0)])
def test_all_actions_strictly_in_local_action_set(pos: int, goal: int) -> None:
    """Bot decisions must strictly remain within the legal course-local action set."""
    state = {"position": pos, "goal": goal, "opponent_position": 2}
    action = choose_action(state)
    assert action in LOCAL_ACTIONS
