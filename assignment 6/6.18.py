div4 = []
div6 = []
div8 = []
div10 = []
div3 = []
div5 = []
div7 = []
div9 = []
for i in range(1, 101):
    if i % 4 == 0:
        div4.append(i)
    if i % 6 == 0:
        div6.append(i)
    if i % 8 == 0:
        div8.append(i)
    if i % 10 == 0:
        div10.append(i)
    if i % 3 == 0:
        div3.append(i)
    if i % 5 == 0:
        div5.append(i)
    if i % 7 == 0:
        div7.append(i)
    if i % 9 == 0:
        div9.append(i)
print(div4)
print(div6)
print(div8)
print(div10)
print(div3)
print(div5)
print(div7)
print(div9)
