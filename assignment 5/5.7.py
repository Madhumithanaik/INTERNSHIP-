s = input()
n = s.find('not')
p = s.find('poor')
if n != -1 and p != -1 and p > n:
    s = s[:n] + 'good' + s[p+4:]
print(s)
