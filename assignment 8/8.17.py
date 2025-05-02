matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
matrix1.sort(key=lambda row: sum(row))
matrix2.sort(key=lambda row: sum(row))
print(matrix1)
print(matrix2)
