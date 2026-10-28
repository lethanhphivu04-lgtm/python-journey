"""Student Bot for the course-local Line Arena.

A transparent, heuristic-driven bot that reasons from structured state,
validates inputs defensively, and explains every action taken.
"""

from __future__ import annotations

LOCAL_ACTIONS = ("left", "right", "wait")
MIN_POSITION = 0
MAX_POSITION = 4


def validate_state(state: dict[str, int] | None) -> bool:
    """Validate that the incoming state dictionary has essential fields."""
    if not isinstance(state, dict):
        return False
    required_keys = ("position", "goal")
    return all(key in state and isinstance(state[key], int) for key in required_keys)


def is_at_goal(position: int, goal: int) -> bool:
    """Check if the bot has already reached its goal."""
    return position == goal


def get_direction_to_goal(position: int, goal: int) -> str:
    """Return the step direction needed to move closer to the goal."""
    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


def assess_tactical_situation(state: dict[str, int]) -> dict[str, int | str]:
    """Extract key metrics from structured state for diagnostic reasoning."""
    pos = state.get("position", 0)
    goal = state.get("goal", pos)
    opp = state.get("opponent_position")

    dist_to_goal = abs(pos - goal)
    dist_to_opp = abs(pos - opp) if isinstance(opp, int) else -1

    return {
        "position": pos,
        "goal": goal,
        "opponent_position": opp if opp is not None else -1,
        "dist_to_goal": dist_to_goal,
        "dist_to_opp": dist_to_opp,
        "step_direction": get_direction_to_goal(pos, goal),
    }


def choose_action(state: dict[str, int]) -> str:
    """Choose a deterministic, legal action based on state heuristics.

    Decision rules in priority order:
    1. Defensive fallback: If state is invalid or missing, safely wait.
    2. Goal achieved: If already at goal, wait to preserve victory.
    3. Forward progress: Advance toward the goal.
    """
    if not validate_state(state):
        return "wait"

    position = state["position"]
    goal = state["goal"]

    # Rule 1: Goal achieved
    if is_at_goal(position, goal):
        return "wait"

    # Rule 2: Move toward goal (Line Arena allows passing through)
    action = get_direction_to_goal(position, goal)
    return action if action in LOCAL_ACTIONS else "wait"


def explain_decision(state: dict[str, int], action: str) -> str:
    """Produce a human-readable explanation of why an action was chosen."""
    if not validate_state(state):
        return f"Action={action!r}: Invalid or missing state, fallback to wait."

    tactics = assess_tactical_situation(state)
    pos = tactics["position"]
    goal = tactics["goal"]
    opp = tactics["opponent_position"]

    if pos == goal:
        return f"Action={action!r}: Already at goal ({pos}), waiting."

    return (
        f"Action={action!r}: At pos={pos}, goal={goal} (dist={tactics['dist_to_goal']}), "
        f"opponent={opp} -> moving toward goal."
    )


def main() -> None:
    """Run a local sanity check demonstrating state reasoning and explanation."""
    teaching_state = {
        "turn": 1,
        "max_turns": 6,
        "position": 0,
        "opponent_position": 4,
        "goal": 4,
        "min_position": MIN_POSITION,
        "max_position": MAX_POSITION,
    }
    action = choose_action(teaching_state)
    explanation = explain_decision(teaching_state, action)
    print(f"Chosen action: {action}")
    print(f"Explanation: {explanation}")


if __name__ == "__main__":
    main()
