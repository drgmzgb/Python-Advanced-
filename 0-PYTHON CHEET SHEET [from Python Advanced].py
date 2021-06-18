# 1. [:] - splitting string into characters
text = 'koi si'
reversed_word = []
reversed_word[:] = text
# ['k', 'o', 'i', ' ', 's', 'i']

#2 Tuples and Sets rotate - rotating a list/counting n times /with deque/:
from collections import deque
players_left = deque(input())
players_left.rotate(-int(input()))
player_out = players_left.pop()

#3 pop/apend
res = input().split().pop()
reversed_res = []
reversed_res.append(res)

#4 deque/append/popleft
from collections import deque
queue = deque(input())
person_to_get_water = queue.popleft()

#5 appendleft
numbers_to_be_added = []
numbers_stack = deque((numbers_to_be_added))
command = input().split()
num_to_be_added = int(command[1])
numbers_stack.appendleft(num_to_be_added)
# using appendleft the same way as append but to add them from the left!

#6 max and min number in an arrey/list
numbers_stack = [1, 2, 3]
max_number = max(numbers_stack)
min_number = min(numbers_stack)

#7 turn list of a string of numbers to a list of numbers
orders = input()
x = [int(n) for n in orders]

# 8 finding the longest list within a list with function max:
intersections = []
final_result = max(intersections, key=lambda coll: len(coll))

# # list(input()):
# from
# # matrix = [
# #   ['ABC'],
# #   ['DEF'],
# #   ['X!@']
# # ]
# to
# [['A', 'B', 'C'], ['D', 'E', 'F'], ['X', '!', '@']]

# 9 matrix in one line with comprehension
n = int(input())
matrix = [[int(el) for el in input().split(", ")] for _ in range(n)]
#
# 10 how to print dictionary with list comprehension - on new rows
result = {}
[print(f'{key} -> {value}') for key, value in result.items()]

# 11 filter even nums with lambda
nums = []
res = list(filter(lambda x: x % 2 == 0, nums))

# 12 print list with integers
for el in final_result:
    print(", ".join(map(str, el)))



