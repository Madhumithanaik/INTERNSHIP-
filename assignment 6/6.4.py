x = int(input())
y = int(input())
z = int(input())
if x == y == z:
    print("Equilateral triangle")
elif x == y or y == z or z == x:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
