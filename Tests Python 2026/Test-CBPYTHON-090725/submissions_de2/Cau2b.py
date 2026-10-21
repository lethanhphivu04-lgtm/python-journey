s = input()
x = int(input())
y = int(input())
vowels = "aeiouAEIOU"
print(sum(1 for ch in s[x - 1:y] if ch in vowels))
