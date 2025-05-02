lst = list(map(int, input().split()))
n = int(input())
if n in lst:
    lst.remove(n)
for i in lst:
    print(i)
