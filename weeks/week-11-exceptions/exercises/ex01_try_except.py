"""Exercise 01: expected bad input."""

# ĐỀ BÀI GỐC (ORIGINAL TODO):
# TODO: catch ValueError from int(raw_turn) and print a useful message.
# TODO: do not add a broad except.

raw_turn = "not-a-number"

try:
    print(int(raw_turn))
except ValueError:
    print(f"'{raw_turn}' is not a valid number")
