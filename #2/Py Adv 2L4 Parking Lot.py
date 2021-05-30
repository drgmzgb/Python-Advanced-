# Py Adv 2L4 Parking Lot - add and discard / set

# input / 4
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# OUT, CA1234TA
# output / Parking Lot is Empty

cars_to_be_out = set()
num = int(input())

for n in range(num):
    in_or_out, number = input().split(", ")
    if "IN" in in_or_out:
        cars_to_be_out.add(number)
    elif "OUT" in in_or_out:
        if number in cars_to_be_out:
            cars_to_be_out.discard(number)
if cars_to_be_out:
    for number in cars_to_be_out:
        print(number)
else:
    print("Parking Lot is Empty")