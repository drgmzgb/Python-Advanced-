# Py Adv 3E4 Matrix Shuffling
# output 5 2 3
# 4 1 6
# Invalid input!
# 5 4 3
# 2 1 6
# input 2 3
# 1 2 3
# 4 5 6
# swap 0 0 1 1
# swap 10 9 8 7
# swap 0 1 1 0
# END

rows, columns = [int(el) for el in input().split()]
matrix = []
for _ in range(rows):
    matrix.append([el for el in input().split()])
command = input()
while "END" not in command:
    if 'swap' in command:
        swap, row1, col1, row2, col2 = command.split()
        if int(row1) <= rows and int(row2) <= rows and int(col1) <= columns and int(col2) <= columns:
            a = matrix[int(row1)][int(col1)]
            b = matrix[int(row2)][int(col2)]
            matrix[int(row1)][int(col1)] = b
            matrix[int(row2)][int(col2)] = a
            for i in range(rows):
                for j in range(columns):
                    print(matrix[i][j], end=' ')
                print()
        else:
            print(f'Invalid input!')
    else:
        print(f"Invalid input!")
    command = input()