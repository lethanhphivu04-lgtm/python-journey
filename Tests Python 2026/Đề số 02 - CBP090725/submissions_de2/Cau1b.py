import unicodedata

def remove_accents(s):
    s = s.replace("đ", "d").replace("Đ", "D")
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")

tinh = input()
ma = input()
print(f"{remove_accents(tinh)} co ma vung {ma}")
