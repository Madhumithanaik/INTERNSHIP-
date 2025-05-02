lst = [1, 'apple', 3.14, 'banana', 10, 2.5]
ints = []
strs = []
floats = []
for i in lst:
    if type(i) == int:
        ints.append(i)
    elif type(i) == float:
        floats.append(i)
    elif type(i) == str:
        strs.append(i)
print(ints)
print(strs)
print(floats)
