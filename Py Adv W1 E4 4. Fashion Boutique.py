# Py Adv W1 E4 4. Fashion Boutique 60% error by softunis
# input
# 5 4 8 6 3 8 7 7 9
# 16
# output
# 5
from collections import deque
clothes = [int(n) for n in input().split()]
max_storing = int(input())
queue_of_clothes = deque(clothes)
n_of_racks = []
to_store = 0
next_clothing_to_be_added = 0
while not len(queue_of_clothes) <= 0:
    first_clothing = queue_of_clothes.popleft()
    to_store = first_clothing
    if len(queue_of_clothes) > 1:
        next_clothing_to_be_added = queue_of_clothes[0]
    while to_store + next_clothing_to_be_added <= max_storing and len(queue_of_clothes) > 0:
        next_clothing = queue_of_clothes.popleft()
        to_store += next_clothing
        if len(queue_of_clothes) > 0:
            next_clothing_to_be_added = queue_of_clothes[0]
        else:
            break
    n_of_racks.append(to_store)
print(len(n_of_racks))

