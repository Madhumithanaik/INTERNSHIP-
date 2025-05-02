total = 0
count = 0
while True:
    n = int(input())
    if n == 0:
        break
    total += n
    count += 1
print("Sum:", total)
print("Average:", total / count)
