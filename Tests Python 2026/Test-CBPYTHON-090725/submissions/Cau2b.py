s = input()
x = int(input())
y = int(input())
sub = s[x - 1:y]
count = sum(1 for ch in sub if ch.isdigit())
print(count)
