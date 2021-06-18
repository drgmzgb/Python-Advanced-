def find_two_closest_nums(x, y, num):
    import sys
    final_numbers = []
    min_abs_dif = sys.maxsize
    for each_el in a:
        for element in b:
            res = each_el + element
            abs_diff = abs(num - res)
            if abs_diff <= min_abs_dif:
                min_abs_dif = abs_diff
                final_numbers.append([abs_diff, each_el, element])

    final_result = []
    current_difference = sys.maxsize
    for row in final_numbers:
        difference = row[0]
        if difference < current_difference:
            current_difference = difference
            final_result = []
            final_result.append([row[1], row[2]])
        elif difference == current_difference:
            current_difference = difference
            final_result.append([row[1], row[2]])

    for el in final_result:
        print(", ".join(map(str, el)))


a = [-1, 3, 8, 2, 9, 5]
b = [4, 1, 2, 10, 5, 20]
target = 24
res = find_two_closest_nums(a, b, target)
