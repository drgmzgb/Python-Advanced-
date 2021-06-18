#Py Adv WI L4 Water Dispancer

# iinput
# 2
# Peter
# Amy
# Start
# 2
# refill 1
# 1
# End
from collections import deque
quantity = int(input())
command = input()
people = []
PeopleAlreadyAdded = False
while not command == "Start":
    people.append(command)
    command = input()
PeopleAlreadyAdded = True
queue = deque(people)
command = input()
while not command == "End":
    if "refill" in command:
        command = command.split()
        quantity += int(command[1])
    else:
        water_needed = int(command)
        if water_needed <= quantity:
            quantity -= water_needed
            person_to_get_water = queue.popleft()
            print(f"{person_to_get_water} got water")
        else:
            person_to_get_water = queue.popleft()
            print(f"{person_to_get_water} must wait")
    command = input()
print(f"{quantity} liters left")