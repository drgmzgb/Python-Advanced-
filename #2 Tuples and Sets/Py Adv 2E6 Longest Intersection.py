# Py Adv 2E6 Longest Intersection - using MAX

# input 3
# 0,3-1,2
# 2,10-3,5
# 6,15-3,10
# output     Longest intersection is [6, 7, 8, 9, 10] with length 5
intersections = []
number = int(input())
for times in range(number):
    first, second = input().split("-")
    first_start, first_end = first.split(",")
    first_set = set()
    for _ in range(int(first_start), int(first_end)+1):
        first_set.add(_)
    # {0, 1, 2, 3}

    second_start, second_end = second.split(",")
    second_set = set()
    # {1, 2}
    for x in range(int(second_start), int(second_end)+1):
        second_set.add(x)

    result = first_set.intersection(second_set)
    result_to_save = [int(el) for el in result]
    intersections.append(result_to_save)
max_intersection = 0
final_result = max(intersections, key=lambda coll: len(coll))
for elements in intersections:
    number_of_intersections = len(elements)
print(f"Longest intersection is {final_result} with length {len(final_result)}")