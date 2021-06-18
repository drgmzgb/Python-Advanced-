# Py Adv 3e5 Snake Moves
# SoftUn
# UtfoSi
# niSoft
# foSinU
# tUniSo
# input 5 6
# SoftUni
index = 0
matrix = []
from collections import deque
rows, cols = [int(el) for el in input().split()]
current_str = input()
current_str = deque(current_str)

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        matrix[row].append("")

for row in range(rows):
    for col in range(cols):
        current_col = col
        index += 1
        txt = current_str.popleft()
        if not row % 2 == 0:
            current_col = cols - 1 - col
        matrix[row][current_col] = txt
        current_str.append(txt)
for row in matrix:
    print("".join(row))