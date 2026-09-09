"""Exercise 01: list create, read, update and delete."""

subjects = ["Toán", "Văn", "Anh"]

# TODO: append one subject and insert another at index 1.
subjects.append("Lý")
subjects.insert(1, "Hóa")

# TODO: update the first subject.
subjects[0] = "Toán Cao Cấp"

# TODO: remove one known subject and pop the last subject.
subjects.remove("Văn")
last = subjects.pop()

# TODO: print the first, last and middle slice after each safe operation.
print("Phần tử đầu:", subjects[0])       # -> Toán Cao Cấp
print("Phần tử cuối:", subjects[-1])     # -> Anh
print("Phần tử giữa:", subjects[1:-1])   # -> ['Hóa']

print(subjects)
# -> Kết quả danh sách cuối cùng: ['Toán Cao Cấp', 'Hóa', 'Anh']
