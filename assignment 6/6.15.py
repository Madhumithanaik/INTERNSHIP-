nums = []
while True:
    val = input()
    if val == 'q':
        break
    nums.append(int(val))
total = sum(nums)
product = 1
for n in nums:
    product *= n
print("Average:", total / len(nums))
print("Product:", product)
