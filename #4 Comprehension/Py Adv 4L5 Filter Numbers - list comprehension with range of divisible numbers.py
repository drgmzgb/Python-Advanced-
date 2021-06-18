# Py Adv 4L5 Filter Numbers - list comprehension with range of divisible numbers
# output [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20]
# input 1
# 20

starting_number = int(input())
ending_number = int(input())
print([num for num in range(starting_number, ending_number+1) if [num2 for num2 in range(2, 11) if num % num2 == 0]])
