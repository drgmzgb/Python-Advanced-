# Py Adv WI E3 3. Fast Food 80% softuni error again.
# input
# 348
# 20 54 30 16 7 9
# output
# 54
# Orders complete
from collections import deque
orders_finished = []
number = int(input())
orders = input().split()
queue = deque(orders)
orders = [int(n) for n in orders]
max_order = max(orders)
print(max_order)
unfinished = []
for nums in range(len(orders)):
    if not nums == max_order:
        current_number = queue.popleft()
        if int(current_number) <= number:
            number -= int(current_number)
        elif int(current_number) > number:
            unfinished.append(current_number)
if unfinished == []:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(unfinished)}")