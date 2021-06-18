# Py Adv 4L3 Even Matrix - matrix with even numbers only
# output [[2], [4, 6]]
# input 2
# 1, 2, 3
# 4, 5, 6

n = int(input())

matrix = [[int(el) for el in input().split(", ") if int(el) % 2 == 0] for _ in range(n)]
print(matrix)

