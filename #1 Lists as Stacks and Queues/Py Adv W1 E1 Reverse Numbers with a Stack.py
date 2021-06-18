# Py Adv W1 E1 Reverse Numbers with a Stack
# input
# 1 2 3 4 5
# output
# 5 4 3 2 1

numbers = input().split()
reversed_nums = []
for times in range(len(numbers)):
    number_out = numbers.pop()
    reversed_nums.append(number_out)
print(" ".join(reversed_nums))