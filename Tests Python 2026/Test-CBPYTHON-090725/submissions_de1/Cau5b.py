def get_high_scores(d, min_score):
    return [name for name, val in d.items() if val >= min_score]

score = {"An": 8, "Binh": 6, "Cuong": 9, "Dung": 5, "Hoa": 8}
print(get_high_scores(score, 8))
