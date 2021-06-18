# Py Adv 3L1 Sum  Matrix Elements
# input 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
# output 76
# [[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]

rows, cols = [int(el) for el in input().split(", ")]
matrix = []
for _ in range(rows):
    matrix.append([int(el) for el in input().split(", ")])
total = 0
for row in range(rows):
    for col in range(cols):
        total += matrix[row][col]
print(total)
print(matrix)