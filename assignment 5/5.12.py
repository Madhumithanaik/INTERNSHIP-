s = input()
if sum(1 for c in s[:4] if c.isupper()) >= 2:
    print(s.upper())
else:
    print(s)
