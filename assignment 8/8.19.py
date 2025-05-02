words = ['red', 'black', 'white', 'green', 'orange']
substring1 = 'ack'
substring2 = 'abc'
result1 = list(filter(lambda x: substring1 in x, words))
result2 = list(filter(lambda x: substring2 in x, words))
print(result1)
print(result2)
