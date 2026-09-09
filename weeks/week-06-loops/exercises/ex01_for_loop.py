"""Exercise 01: for, range, enumerate and zip."""

topics = ["loops", "enumerate", "zip"]
scores = [7, 8, 9]

# TODO: print numbers 1 through 5 with range.
for i in range(1, 6):
    print(i)
# -> Kết quả: 1, 2, 3, 4, 5 lần lượt trên mỗi dòng

# TODO: print each topic with a one-based position using enumerate.
for idx, topic in enumerate(topics, start=1):
    print(f"{idx}. {topic}")
# -> Kết quả:
# 1. loops
# 2. enumerate
# 3. zip

# TODO: pair topics and scores with zip(..., strict=True).
for topic, score in zip(topics, scores, strict=True):
    print(f"{topic}: {score}")
# -> Kết quả:
# loops: 7
# enumerate: 8
# zip: 9

print(topics, scores)
