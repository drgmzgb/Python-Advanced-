# Py Adv 3E3 Maximal Sum 3 x 3 max sum
# Output Sum = 75
# 1 4 14
# 7 11 2
# 8 12 16
# Input 4 5
# 1 5 5 2 4
# 2 1 4 14 3
# 3 7 11 2 8
# 4 8 12 16 4

import sys

sum_max = -sys.maxsize
rows, columns = [int(el) for el in input().split()]
matrix = []
for _ in range(rows):
    matrix.append([int(el) for el in input().split()])

for row in range(rows-2):
    for column in range(columns-2):
        a = matrix[row][column]
        b = matrix[row][column+1]
        c = matrix[row][column+2]
        d = matrix[row+1][column]
        e = matrix[row+1][column+1]
        f = matrix[row+1][column+2]
        g = matrix[row+2][column]
        h = matrix[row+2][column+1]
        i = matrix[row+2][column+2]
        result = a+b+c+d+e+f+g+h+i
        if result >= sum_max:
            sum_max = result
            position = row, column

(row_of_max, column_of_max) = position
print(f'Sum = {sum_max}')

# for _ in range(row_of_max):
#     a = matrix[row][column]
#     b = matrix[row][column + 1]
#     c = matrix[row][column + 2]
#     d = matrix[row + 1][column]
#     e = matrix[row + 1][column + 1]
#     f = matrix[row + 1][column + 2]
#     g = matrix[row + 2][column]
#     h = matrix[row + 2][column + 1]
#     i = matrix[row + 2][column + 2]
#     print(f'{a} {b} {c}')
#     print(f'{d} {e} {f}')
#     print(f'{g} {h} {i}')

for _ in range(1):
    a = matrix[row_of_max][column_of_max]
    b = matrix[row_of_max][column_of_max + 1]
    c = matrix[row_of_max][column_of_max + 2]
    d = matrix[row_of_max + 1][column_of_max]
    e = matrix[row_of_max + 1][column_of_max + 1]
    f = matrix[row_of_max + 1][column_of_max + 2]
    g = matrix[row_of_max + 2][column_of_max]
    h = matrix[row_of_max + 2][column_of_max + 1]
    i = matrix[row_of_max + 2][column_of_max + 2]
    print(f'{a} {b} {c}')
    print(f'{d} {e} {f}')
    print(f'{g} {h} {i}')