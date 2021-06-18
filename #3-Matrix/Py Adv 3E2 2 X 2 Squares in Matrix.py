# Py Adv 3E2 2 X 2 Squares in Matrix
# output 2
# input 3 4
# A B B D
# E B B B
# I J B B

sum_of_equal_squares = 0

rows, columns = [int(el) for el in input().split()]
matrix = []
for _ in range(rows):
    matrix.append([el for el in input().split()])

for row in range(rows-1):
    for column in range(columns-1):
        a = matrix[row][column]
        b = matrix[row][column+1]
        c = matrix[row+1][column]
        d = matrix[row+1][column+1]
        if a == b == c == d:
            sum_of_equal_squares += 1
print(sum_of_equal_squares)