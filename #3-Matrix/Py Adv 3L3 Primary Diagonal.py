# Py Adv 3L3 Primary Diagonal
# input 3
# 11 2 4
# 4 5 6
# 10 8 -12
# output 4
sum_in_total = 0
n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(el) for el in input().split()])
for n in range(n):
    number = matrix[n][n]
    sum_in_total += int(number)
print(sum_in_total)