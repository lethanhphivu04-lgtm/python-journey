"""Exercise 02: defensive validation."""

LOCAL_ACTIONS = {"left", "right", "wait"}


# ĐỀ BÀI GỐC (ORIGINAL TODO):
# TODO: raise ValueError for an action outside LOCAL_ACTIONS.
# (Bắn lỗi ValueError nếu action truyền vào nằm ngoài tập hợp LOCAL_ACTIONS)
def validate_action(action: str) -> str:
    if action not in LOCAL_ACTIONS:
        raise ValueError(f"illegal local action: {action!r}")
    return action


print(validate_action("wait"))
