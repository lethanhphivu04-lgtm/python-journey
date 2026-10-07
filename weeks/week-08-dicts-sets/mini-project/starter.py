"""Starter for the Week 08 Decision Dashboard."""

REQUIRED_FIELDS = {"position", "goal"}
LOCAL_ACTIONS = {"left", "right", "wait"}


def validate_state(state: dict[str, object]) -> bool:
    """Return whether all required fields exist."""
    return REQUIRED_FIELDS.issubset(state.keys())


def summarize_state(state: dict[str, object]) -> str:
    """Return a short learner-readable summary."""
    pos = state.get("position", "?")
    goal = state.get("goal", "?")
    opp = state.get("opponent_position", "không có")
    return f"Vị trí: {pos} | Mục tiêu: {goal} | Đối thủ: {opp}"


def recommend_action(state: dict[str, object]) -> str:
    """Return one recommendation from 2–4 explainable rules."""
    if not validate_state(state):
        return "wait"
    pos = int(state["position"])
    goal = int(state["goal"])
    opp = state.get("opponent_position")

    if pos == goal:
        return "wait"
    if opp is not None and abs(pos - int(opp)) <= 1:
        return "wait"
    return "right" if pos < goal else "left"


def main() -> None:
    """Run the dashboard on a small nested teaching model."""
    dashboard = {
        "state": {
            "position": 1,
            "opponent_position": 3,
            "goal": 4,
        },
        "tags": {"course-local", "week-08"},
    }
    state = dashboard["state"]
    if not isinstance(state, dict):
        print("State không hợp lệ")
        return

    print("COURSE TEACHING MODEL")
    print("NOT VUACOC PRODUCTION CONTRACT")
    print(f"valid={validate_state(state)}")
    print(summarize_state(state))
    action = recommend_action(state)
    print(f"action={action}, legal={action in LOCAL_ACTIONS}")

    # Boundary cases: thiếu optional field, và thiếu required field
    print("\n--- Test boundary cases ---")
    missing_optional = {"position": 2, "goal": 0}
    print("Missing optional:", summarize_state(missing_optional), "-> action:", recommend_action(missing_optional))

    missing_required = {"position": 2}
    print("Missing required: valid =", validate_state(missing_required), "-> action:", recommend_action(missing_required))


if __name__ == "__main__":
    main()
