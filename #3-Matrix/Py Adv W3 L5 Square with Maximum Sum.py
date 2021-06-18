# Py Adv W3 L5 Square with Maximum Sum

# input 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
# output 9 8
# 7 9
# 33

# Write a program that reads a matrix from the console.
# On first line you will get matrix sizes in format "{rows}, {columns}".
# On the next rows, you will get elements for each column separated with a ", ".
# Find the 2x2 top-left submatrix
# with biggest sum of its values.
# Print the matrix and the sum of its elements as shown in the examples.
import sys
matrix = []
max_sum = -sys.maxsize
row, column = [int(el) for el in input().split(", ")]
for _ in range(row):
    matrix.append([int(el) for el in input().split(", ")])
position = None
for row in range(row-1, 0, -1):
    for column in range(column-1, 0, -1):
        a = matrix[row][column]
        b = matrix[row][column-1]
        c = matrix[row-1][column]
        d = matrix[row-1][column-1]
        current_sum = a + b + c + d
        if current_sum >= max_sum:
            max_sum = current_sum
            position = (row, column)
row, col = position
print(matrix[row-1][col-1], matrix[row-1][col])
print(matrix[row][col-1], matrix[row][col])
print(max_sum)