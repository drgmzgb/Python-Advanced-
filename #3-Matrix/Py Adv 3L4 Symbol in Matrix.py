# Py Adv 3L4 Symbol in Matrix
# input 3
# ABC
# DEF
# X!@
# !
# output (2, 1)
position = None
n = int(input())
matrix = []
for _ in range(n):
    matrix.append([n for n in list(input())])
special_symbol = input()

current_symbol = None
for row in range(n):
    for col in range(n):
        if matrix[row][col] == special_symbol:
            position = (row, col)
            break
    if position:
        break
if position:
    print(position)
else:
    print(f'{special_symbol} does not occur in the matrix')