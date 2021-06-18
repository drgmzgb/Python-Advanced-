# Py Adv 4L4 Flattening Matrix - combining elements of matrix in one list, writing matrix comprehension in one line
#
# output [1, 2, 3, 4, 5, 6]
# input 2
# 1, 2, 3
# 4, 5, 6
#

# #matrix2 = [i for i in range(int(input()))]
# matrix = []
# n = int(input())
# for _ in range(n):
#     matrix.append([int(el) for el in input().split(", ")])
# print(matrix)
n = int(input())
# matrix2 = [int(el) for _ in range(int(input())) for el in input().split(", ")]
matrix = [[int(el) for el in input().split(", ")] for _ in range(n)]
matrix2 = [num for sublist in matrix for num in sublist]

print(matrix2)