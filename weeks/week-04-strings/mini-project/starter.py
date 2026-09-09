"""Starter for the Week 04 Text Analyzer."""

import re

while True:
    text = input("Text: ").strip()
    if text:
        break
    print("Text không được để trống, vui lòng nhập lại!")

normalized = " ".join(text.lower().split())
words = normalized.split()
codes = re.findall(r"PJ-\d{3}", text)
print(f"normalized={normalized}")
print(f"characters={len(normalized)}")
print(f"words={len(words)}")
print(f"python_count={normalized.count('python')}")
print(f"course_codes={codes}")
# -> Kết quả mẫu ('Học  PYTHON pj-001  cùng  PJ-002'):
# normalized=học python pj-001 cùng pj-002
# characters=34
# words=5
# python_count=1
# course_codes=['PJ-001', 'PJ-002']
