s = 'thequickbrownfoxjumpsoverthelazydog'
d = {}
for c in s:
    d[c] = d.get(c, 0) + 1
for k in d:
    if d[k] > 1:
        print(k, d[k])
