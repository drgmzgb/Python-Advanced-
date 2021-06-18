# Py Adv 3E1 Diagonal Difference
# output 15
# input 3
# 11 2 4
# 4 5 6
# 10 8 -12
diagonal_sum = 0
diagonal_sum_2 = 0
difference = 0
n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(el) for el in input().split()])

for element in range(n):
    diagonal_sum += matrix[element][element]
for element_2 in range(n):
    diagonal_sum_2 += matrix[element_2][(n-1)-element_2]

difference = abs(diagonal_sum_2 - diagonal_sum)
print(difference)