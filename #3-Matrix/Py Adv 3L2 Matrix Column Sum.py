# Py Adv 3L2 Matrix Column Sum
# input 3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0
# output 12
# 10
# 19
# 20
# 8
# 7

rows, cols = [int(el) for el in input().split(", ")]
matrix = []
total_sum = 0
for row in range(int(rows)):
    matrix.append([int(el) for el in input().split()])

for col in range(cols):
    for row in range(rows):
        num_1 = matrix[row][col]
        total_sum += num_1
    print(total_sum)
    total_sum = 0

