# Py Adv 4E8 hEROES iNVENTORY
# OUTPUT Peter -> Items: 2, Cost: 30
# George -> Items: 2, Cost: 120
# input
# Peter, George
# Peter-Sword-20
# Peter-Shield-10
# George-Gem-100
# Peter-Sword-15
# George-Sword-20
# End

names = input().split(", ")
command = input()
heroes = {n: {} for n in names}
while not command == 'End':
    name, item, cost = command.split("-")
    if item not in heroes[name]:
        heroes[name][item] = cost
    command = input()
current_sum = 0
for name in heroes:
    for value in heroes[name].values():
        current_sum += int(value)
    print(f'{name} -> Items: {len(heroes[name])}, Cost: {current_sum}')
    current_sum = 0