"""Exercise 03: reproduce and fix a defect."""


# ĐỀ BÀI GỐC (ORIGINAL TODO):
# TODO: reproduce with (1, 4), fix the subtraction and retain an assertion.
def distance(position: int, goal: int) -> int:
    result = abs(goal - position)
    assert result >= 0, "Distance cannot be negative"
    return result


print(distance(1, 4))
