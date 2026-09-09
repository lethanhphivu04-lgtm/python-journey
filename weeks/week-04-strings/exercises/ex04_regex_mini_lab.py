"""Exercise 04: a small regular-expression lab."""

import re

text = "Tickets PJ-101 and PJ-205 are open; XX-999 is unrelated."

# TODO 1: use re.findall and r"PJ-\d{3}" to extract both course codes.
codes: list[str] = re.findall(r"PJ-\d{3}", text)
# -> Kết quả: ['PJ-101', 'PJ-205']

# TODO 2: use re.search to find the first number sequence.
match = re.search(r"\d+", text)
first_number = match.group() if match else None
# -> Kết quả: 101

# TODO 3: use re.fullmatch to validate W followed by exactly two digits.
candidate = "W04"
is_week_code = bool(re.fullmatch(r"W\d{2}", candidate))
# -> Kết quả: True

print(codes)
print(first_number)
print(is_week_code)
