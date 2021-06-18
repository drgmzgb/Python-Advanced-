# Py Adv4E4 Number classification-print with join in a dict comprehension with str(x)
# output Positive: 1, 0, 5, 3, 4, 12, 19
# Negative: -2, -100, -20, -33
# Even: -2, 0, 4, -100, -20, 12
# Odd: 1, 5, 3, 19, -33
# input 1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33

all_numbers = [int(num) for num in input().split(', ')]
positive = [num for num in all_numbers if num >= 0]
negative = [num for num in all_numbers if num < 0]
odd = [num for num in all_numbers if not num % 2 == 0]
even = [num for num in all_numbers if num % 2 == 0]
print(f'Positive: {", ".join([str(x) for x in positive])}')
print(f'Negative: {", ".join([str(x) for x in negative])}')
print(f'Even: {", ".join([str(x) for x in even])}')
print(f'Odd: {", ".join([str(x) for x in odd])}')