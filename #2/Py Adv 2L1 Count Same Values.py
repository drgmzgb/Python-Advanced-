# Py Adv 2L1 Count Same Values - find the numbers with dictionary

# You will be given numbers separated by a space. Write a program which prints
# the number of occurrences of each number in the format "{number} - {count} times"

# input -2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3
# output -2.5 - 3 times
# 4.0 - 2 times
# 3.0 - 4 times
# -5.5 - 1 times
dict = {}
numbers = input().split()
numbers = [float(el) for el in numbers]
# [-2.5, 4.0, 3.0, -2.5, -5.5, 4.0, 3.0, 3.0, -2.5, 3.0]

for element in numbers:
    if element not in dict:
        dict[element] = 0
    dict[element] += 1
# {-2.5: 3, 4.0: 2, 3.0: 4, -5.5: 1}

for number, times in dict.items():
    print(f"{number} - {times} times")
