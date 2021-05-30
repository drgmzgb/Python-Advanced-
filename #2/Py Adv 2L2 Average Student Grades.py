# Py Adv 2L2 Average Student Grades - using dictionaries, average

# input / 4
# Scott 4.50
# Ted 3.00
# Scott 5.00
# Ted 3.66
# output / Ted -> 3.00 3.66 (avg: 3.33)
# Scott -> 4.50 5.00 (avg: 4.75)

grades = int(input())
res = {}
for n in range(grades):
    name, grade = input().split()
    if name not in res:
        res[name] = []
    res[name].append(f'{(float(grade)):.2f}')
# {'Peter': [5.2, 3.2], 'Mark': [5.5, 2.5, 3.46], 'Alex': [2.0, 3.0]}

for name, grade in res.items():
    their_sum = 0
    for each_grade in grade:
        their_sum += float(each_grade)
    avg = f"{their_sum / len(grade):.2f}"


    print(f'{name} -> {(" ".join(map(str, grade)))} (avg: {avg})')