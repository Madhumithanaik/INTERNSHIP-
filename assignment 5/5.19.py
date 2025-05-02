s = input()
words = s.split()
print(min(words, key=len))
print(max(words, key=len))
