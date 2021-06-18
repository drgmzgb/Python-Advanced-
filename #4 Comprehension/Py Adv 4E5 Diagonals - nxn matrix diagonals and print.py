# Py Adv 4E5 Diagonals - nxn matrix diagonals and print
# output First diagonal: 1, 5, 9. Sum: 15
# Second diagonal: 3, 5, 7. Sum: 15
# input 3
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
# 2
# 1, 1
# 1, 1
n = int(input())
matrix = [[int(el) for el in input().split(", ")] for _ in range(n)]
primary_diagonal = [matrix[times][times] for times in range(n)]
secondary_diagonal = [matrix[x][(n-1)-x] for x in range(n)]

print(f'First diagonal: {", ".join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}')
print(f'Second diagonal: {", ".join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}')


