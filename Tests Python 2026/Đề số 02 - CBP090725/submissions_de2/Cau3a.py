lst = [100, "apple", 3.14, "banana", 200, None]
print([x for x in lst if isinstance(x, (int, float))])
