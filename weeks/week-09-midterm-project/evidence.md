# Midterm evidence

## Project

- Project name: Midterm Foundations Showcase (Bot V1 & Student Manager)
- Chosen track: Both (Track A: VuaCóc Bot V1 + Track B: Student Manager)
- Commit SHA: Working tree ready (main branch)
- Run command:
  - Track A: `python weeks/week-09-midterm-project/starter/vuacoc_bot_v1.py`
  - Track B: `python weeks/week-09-midterm-project/starter/student_manager.py`
  - Reference Evaluator: `python weeks/week-09-midterm-project/reference/evaluate_baselines.py`

## Design

- Data model:
  - Bot V1: `dict[str, int]` biểu diễn structured state gồm `position`, `goal`, `opponent_position`.
  - Student Manager: `list[dict[str, object]]` biểu diễn danh sách học sinh lồng nhau (`name: str`, `scores: list[float]`).
- Core functions:
  - Bot V1: `choose_action(state)`, `explain_action(state, action)`.
  - Student Manager: `calculate_average(student)`, `classify_student(average)`, `find_student(students, query)`, `generate_report(students)`.
- Bot rules (Bot V1):
  1. Nếu `position == goal`: trả `"wait"` (đã đạt mục tiêu).
  2. Nếu `opponent is not None` và khoảng cách $\le 1$: trả `"wait"` (tránh va chạm gần).
  3. Nếu `position < goal`: trả `"right"` (tiến về đích).
  4. Còn lại: trả `"left"`.

## Baseline results — Bot V1 only

| Opponent | Result | Turn count | Observed strength | Observed weakness |
|---|---|---:|---|---|
| WaitBot | draw | 6 | Returned legal actions until termination | Uses only distance and goal direction |
| ForwardBot | B | 4 | Returned legal actions until termination | Did not reach its goal before the opponent |
| CautiousBot | draw | 6 | Returned legal actions until termination | Uses only distance and goal direction |

*Ghi chú: Đấu trong môi trường Local Arena teaching model, không tính rating/win-rate.*

## Debug evidence

- One bug encountered: Lỗi `ZeroDivisionError` khi tính trung bình danh sách điểm rỗng `[]` và khi lớp học chưa có học sinh nào.
- How it was fixed: Bổ sung guard clause kiểm tra rỗng ở đầu hàm:
  `if not isinstance(scores, list) or not scores: return 0.0`
  và `if not students: return "Danh sách rỗng"`.
- Case rerun after the fix: Case `Châu` có `scores: []` trả về `0.0` an toàn; gọi `generate_report([])` trả về `"Danh sách rỗng"` mà không crash.

## Reflection

- Known weakness: 
  - Bot V1 là heuristic tham lam 1 bước (greedy 1-step), chưa tính toán trước nhiều lượt nước đi hay chủ động chặn đường đối thủ.
  - Student Manager chỉ lưu trữ dữ liệu in-memory, mất dữ liệu khi tắt chương trình.
- Next improvement: 
  - Tích hợp File I/O (CSV/JSON) ở Tuần 10 để lưu trữ dữ liệu bền vững.
  - Chuyển đổi mô hình dữ liệu thành Class OOP ở Tuần 14.
- AI usage disclosure: Sử dụng AI để hỗ trợ kiểm tra các ca biên (boundary checks), định dạng tài liệu bằng chứng theo chuẩn syllabus và chạy lệnh kiểm thử tự động.
