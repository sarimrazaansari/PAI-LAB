# Name: Sarim Raza Ansari
# Roll number: 25K-0064
# Question number: 12

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose = [[matrix[row][column] for row in range(len(matrix))] for column in range(len(matrix[0]))]

row_sums = [sum(row) for row in matrix]
column_sums = [sum(matrix[row][column] for row in range(len(matrix))) for column in range(len(matrix[0]))]

print("Matrix:")
for row in matrix:
    print(row)

print("Transpose:")
for row in transpose:
    print(row)

print("Row sums:", row_sums)
print("Column sums:", column_sums)
