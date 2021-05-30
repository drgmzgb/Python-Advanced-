# Py Adv W1 E2 2. Maximum and Minimum Element 80% unknown error by SoftUni
# using appendleft, min() and max() in a list

# input
# 9
# 1 97
# 2
# 1 20
# 2
# 1 26
# 1 20
# 3
# 1 91
# 4
# output
# 26
# 20
# 91, 20, 26
numbers_to_be_added = []
n_times = int(input())
from collections import deque
final_collection = []
numbers_stack = deque(numbers_to_be_added)
for n in range(n_times):
    command = input()
    if len(command) > 1:
        command = command.split()
        num_to_be_added = int(command[1])
        numbers_stack.appendleft(num_to_be_added)
    elif int(command) == 2:
        if len(numbers_stack) >= 1:
            numbers_stack.popleft()
    elif int(command) == 3:
        if len(numbers_stack) >= 1:
            max_number = max(numbers_stack)
            print(max_number)
    elif int(command) == 4:
        if len(numbers_stack) >= 1:
            min_number = min(numbers_stack)
            print(min_number)
for element in numbers_stack:
    final_collection.append(str(element))
print(", ".join(final_collection))
