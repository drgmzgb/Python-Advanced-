# Py Adv 2L3 Record Unique Names = set - printing set/string

# input / 8
# Lee
# Joey
# Lee
# Joe
# Alan
# Alan
# Peter
# Joey
# output / Alan
# Joey
# Lee
# Joe
# Peter
times = int(input())
unique_names = set()

for n in range(times):
    name = input()
    unique_names.add(name)

for el in unique_names:
    print("".join(el))