lst = [100, "apple", 3.14, "banana", 200, None]
new_lst = [item for item in lst if isinstance(item, str)]
print(new_lst)
