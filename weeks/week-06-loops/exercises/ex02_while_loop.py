"""Exercise 02: while, break and continue."""

remaining = 5

# TODO: count down to 1 and update remaining on every pass.
while remaining > 0:
    print(remaining)
    remaining -= 1
# -> Kết quả: 5, 4, 3, 2, 1

# TODO: loop through 1..10, skip multiples of 3 and stop after 8.
num = 1
while num <= 10:
    if num > 8:
        break
    if num % 3 == 0:
        num += 1
        continue
    print("selected:", num)
    num += 1
# -> Kết quả:
# selected: 1
# selected: 2
# selected: 4
# selected: 5
# selected: 7
# selected: 8

print(remaining)
# -> Kết quả: 0
