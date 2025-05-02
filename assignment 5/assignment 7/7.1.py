dict1 = {0: 10, 1: 20, 2: 15}
sorted_dict_asc = dict(sorted(dict1.items(), key=lambda item: item[1]))
print("Sorted Dictionary (Ascending):", sorted_dict_asc)
sorted_dict_desc = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
print("Sorted Dictionary (Descending):", sorted_dict_desc)
