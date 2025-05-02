list1 = [{}, {}, {}]
list2 = [{1, 2}, {}, {}]
all_empty1 = all(not d for d in list1)
all_empty2 = all(not d for d in list2)
print("All dictionaries empty in list1:", all_empty1)
print("All dictionaries empty in list2:", all_empty2)
