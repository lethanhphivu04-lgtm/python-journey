"""Starter for the course-local VuaCóc Bot V1 midterm track."""

LOCAL_ACTIONS = {"left", "right", "wait"}


def choose_action(state: dict[str, int]) -> str:
    """Return a deterministic course-local action from 2–4 explainable rules."""
    position = state.get("position", 0)
    goal = state.get("goal", position)
    opponent = state.get("opponent_position")

    if position == goal:
        return "wait"
    if opponent is not None and abs(position - opponent) <= 1:
        return "wait"
    return "right" if position < goal else "left"


def explain_action(state: dict[str, int], action: str) -> str:
    """Explain which observed state values led to an action."""
    pos = state.get("position", "?")
    goal = state.get("goal", "?")
    opp = state.get("opponent_position", "none")
    return f"position={pos}, goal={goal}, opponent={opp} -> action={action}"


def main() -> None:
    """Smoke-test representative course-local states."""
    test_cases = [
        {"position": 0, "opponent_position": 4, "goal": 4},  # Normal advance
        {"position": 4, "opponent_position": 2, "goal": 4},  # Goal reached
        {"position": 2, "opponent_position": 3, "goal": 4},  # Opponent near
        {"position": 3, "goal": 0},                          # Moving left, no opponent
    ]
    print("COURSE TEACHING MODEL")
    print("NOT VUACOC PRODUCTION CONTRACT")
    for state in test_cases:
        action = choose_action(state)
        print(explain_action(state, action), f"| legal={action in LOCAL_ACTIONS}")


if __name__ == "__main__":
    main()
