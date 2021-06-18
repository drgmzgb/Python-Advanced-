# Py Adv 2E4 Count Symbols - dictionaries

# input SoftUni rocks
# output  : 1 time/s
# S: 1 time/s
# U: 1 time/s
# c: 1 time/s
# f: 1 time/s
# i: 1 time/s
# k: 1 time/s
# n: 1 time/s
# o: 2 time/s
# r: 1 time/s
# s: 1 time/s
# t: 1 time/s

characters = set()
times = {}
command = input()
for element in command:
    characters.add(element)
    if element not in times:
        times[element] = 0
    times[element] += 1
# result = sorted(times)
sorted_nums = sorted(times, key=lambda kvp: kvp[0])
for el in sorted_nums:
    for key, value in times.items():
        if key == el:
            print(f"{el}: {value} time/s")