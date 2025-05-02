held = int(input())
attended = int(input())
percent = (attended / held) * 100
print("Attendance:", percent)
if percent >= 75:
    print("Allowed to sit")
else:
    print("Not allowed to sit")
