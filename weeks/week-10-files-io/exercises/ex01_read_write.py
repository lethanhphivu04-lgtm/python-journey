"""Exercise 01: pathlib and UTF-8 text."""

from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
path = WEEK_ROOT / ".learner-output" / "week10.txt"

# Tạo thư mục cha nếu chưa tồn tại
path.parent.mkdir(parents=True, exist_ok=True)

# Ghi hai dòng với encoding="utf-8"
lines = [
    "Line 1: Python Journey - Week 10 Data Persistence",
    "Line 2: Working with pathlib and UTF-8 encoding",
]
path.write_text("\n".join(lines) + "\n", encoding="utf-8")

# Đọc text và in từng dòng với số thứ tự bắt đầu từ 1
content = path.read_text(encoding="utf-8")
for index, line in enumerate(content.splitlines(), start=1):
    print(f"{index}: {line}")

print(f"File saved at: {path}")
