# Py Adv 2E7 Battle of Names

# input 4
# Pesho
# Stefan
# Stamat
# Gosho
# output 304, 128, 206, 511
num = int(input())
row = 0
results_odd = set()
results_even = set()
for n in range(num):
    row += 1
    characters_sum = 0
    name = input()
    for el in name:
        character_value = ord(el)
        characters_sum += character_value
    result = characters_sum / row
    if int(result) % 2 == 0:
        results_odd.add(int(result))
    else:
        results_even.add(int(result))
sum_elements_odd = 0
sum_elements_even = 0
for element in results_odd:
    sum_elements_odd += element
for elements in results_even:
    sum_elements_even += elements

if sum_elements_odd == sum_elements_even:
    final_result = results_odd.union(results_even)

if sum_elements_odd > sum_elements_even:
    final_result = results_odd.difference(results_even)

if sum_elements_odd < sum_elements_even:
    final_result = results_odd.symmetric_difference(results_even)

for each_num in final_result:
    print(int(each_num), end=", ")
