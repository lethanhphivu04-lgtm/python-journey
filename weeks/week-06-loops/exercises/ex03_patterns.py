"""Exercise 03: readable list comprehensions."""

numbers = range(1, 11)

# TODO: build squares for all numbers.
squares: list[int] = [n**2 for n in numbers]
# -> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# TODO: build even_numbers with one filter.
even_numbers: list[int] = [n for n in numbers if n % 2 == 0]
# -> [2, 4, 6, 8, 10]

# TODO: rewrite one comprehension as a normal loop and compare readability.
evens_loop = []
for n in numbers:
    if n % 2 == 0:
        evens_loop.append(n)

print(squares, even_numbers)
# -> Kết quả:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] [2, 4, 6, 8, 10]
