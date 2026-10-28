"""Complete these learner tests."""

import sys
from pathlib import Path

# Đảm bảo đường dẫn import hoạt động khi chạy từ root hoặc trong thư mục exercises
_EXERCISES_DIR = Path(__file__).resolve().parent
if str(_EXERCISES_DIR) not in sys.path:
    sys.path.insert(0, str(_EXERCISES_DIR))

# pyrefly: ignore[missing-import]
import pytest  # noqa: E402
# pyrefly: ignore[missing-import]
from decision import LOCAL_ACTIONS, choose_action, validate_turn  # noqa: E402


def test_normal_case() -> None:
    # ĐỀ BÀI GỐC (ORIGINAL TODO):
    # TODO: Arrange position/goal, Act, then Assert the expected action.
    # Arrange: Chuẩn bị dữ liệu đầu vào (vị trí hiện tại < vị trí đích)
    position, goal = 1, 4

    # Act: Gọi hàm cần kiểm thử
    action = choose_action(position, goal)

    # Assert: Kiểm tra bot đi sang phải và thuộc tập hợp hành động hợp lệ
    assert action == "right"
    assert action in LOCAL_ACTIONS


def test_edge_case_at_goal() -> None:
    # ĐỀ BÀI GỐC (ORIGINAL TODO):
    # TODO: assert the bot waits at its goal.
    # Trường hợp biên: Khi bot đã ở vị trí đích (position == goal) -> bot phải đứng chờ ("wait")
    assert choose_action(4, 4) == "wait"


def test_invalid_turn() -> None:
    # ĐỀ BÀI GỐC (ORIGINAL TODO):
    # TODO: use pytest.raises(ValueError) for validate_turn(0).
    # Trường hợp dữ liệu không hợp lệ: turn < 1 phải bắn ra ngoại lệ ValueError
    with pytest.raises(ValueError, match="positive"):
        validate_turn(0)


def test_regression_position_past_goal_moves_left() -> None:
    # ĐỀ BÀI GỐC (ORIGINAL TODO):
    # Regression: an earlier version always returned "right".
    # Ca kiểm thử hồi quy: Khi bot đi quá đích (position > goal), bot phải quay lại sang trái ("left")
    assert choose_action(4, 1) == "left"
