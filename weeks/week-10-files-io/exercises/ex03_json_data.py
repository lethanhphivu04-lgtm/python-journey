"""Exercise 03: JSON-compatible replay data."""

import json
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
path = WEEK_ROOT / ".learner-output" / "replay.json"
replay = {
    "format": "COURSE LOCAL FORMAT",
    "production_compatibility": "NOT VUACOC PRODUCTION FORMAT",
    "turns": [],
}

# Tạo thư mục cha trước khi ghi file
path.parent.mkdir(parents=True, exist_ok=True)

# Lưu replay với ensure_ascii=False và indent=2
path.write_text(
    json.dumps(replay, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

# Tải lại và kiểm tra cả hai nhãn trước khi đọc turns
data = json.loads(path.read_text(encoding="utf-8"))
if not isinstance(data, dict):
    raise ValueError("Expected a JSON object")

if (
    data.get("format") != "COURSE LOCAL FORMAT"
    or data.get("production_compatibility") != "NOT VUACOC PRODUCTION FORMAT"
):
    raise ValueError("Replay missing required course labels")

turns = data.get("turns", [])
print(f"Format: {data['format']}")
print(f"Production compatibility: {data['production_compatibility']}")
print(f"Turns count: {len(turns)}")
print(f"JSON saved at: {path}")
