q = int(input())
cost = q * 100
if cost > 1000:
    cost -= cost * 0.1
print("Total cost:", cost)
