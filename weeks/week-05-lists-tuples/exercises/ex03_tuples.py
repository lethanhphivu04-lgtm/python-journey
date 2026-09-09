"""Exercise 03: tuple, packing and unpacking."""

coordinate = (3, 7)

# TODO: unpack coordinate into x and y.
x, y = coordinate
# -> x = 3, y = 7

# TODO: pack name, age and topic into one profile tuple, then unpack it.
profile: tuple[str, int, str] = ("Lê Thanh Phi Vũ", 20, "Python")
ten, tuoi, mon = profile
# -> ten = 'Lê Thanh Phi Vũ', tuoi = 20, mon = 'Python'

# TODO: swap left and right using unpacking.
left = "A"
right = "B"
left, right = right, left
# -> left = 'B', right = 'A'

print(x, y, profile, left, right)
# -> Kết quả: 3 7 ('Lê Thanh Phi Vũ', 20, 'Python') B A
