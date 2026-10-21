"""Exercise 02: CSV match summary."""

import csv
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
path = WEEK_ROOT / ".learner-output" / "match_summary.csv"
rows = [{"bot": "student", "wins": 2}, {"bot": "wait", "wins": 0}]

# Tạo thư mục cha trước khi mở file
path.parent.mkdir(parents=True, exist_ok=True)

# Ghi header và rows bằng csv.DictWriter
with path.open("w", newline="", encoding="utf-8") as stream:
    writer = csv.DictWriter(stream, fieldnames=["bot", "wins"])
    writer.writeheader()
    writer.writerows(rows)

# Tải rows bằng csv.DictReader rồi in kết quả
with path.open(encoding="utf-8") as stream:
    reader = csv.DictReader(stream)
    loaded_rows = list(reader)

for row in loaded_rows:
    print(row)

print(f"CSV saved at: {path}")
