# Py Adv 4E9 Bunker
# output Count of items: 25
# Average quality: 8.00
# food -> pizza, burgers
# water -> mineral
# materials -> wood
# metal -> copper
# input food, water, materials, metal
# 5
# food - pizza - quantity:10;quality:5
# water - mineral - quantity:5;quality:10
# materials - wood - quantity:2;quality:5
# metal - copper - quantity:3;quality:10
# food - burgers - quantity:5;quality:2
total_quantity = 0
total_quality = 0
average_quality = 0
categories = input().split(', ')
n = int(input())
categories_dict = {}
for times in range(n):
    command = input()
    category, item_name, info = command.split(' - ')
    info1, info2 = info.split(';')
    quantity, number_of_quantity = info1.split(':')
    quality, number_of_quality = info2.split(':')
    if category in categories:
        total_quantity += int(number_of_quantity)
        total_quality += int(number_of_quality)
        if category not in categories_dict:
            categories_dict[category] = []
        categories_dict[category].append(item_name)
average_quality = total_quality / len(categories_dict)
print(f'Count of items: {total_quantity}')
print(f'Average quality: {average_quality:.2f}')
for category, itemname in categories_dict.items():
    print(f'{(category)} -> {", ".join(itemname)}')
# [print(f'{", ".join(category)} -> {", ".join(item_name)}' for category, item_name in categories_dict.items())]
#
