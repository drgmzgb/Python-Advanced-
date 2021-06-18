# Py Adv 5E3 Negative vs Positive
# output -189
# 137
# The negatives are stronger than the positives
# input 1 2 -3 -4 65 -98 12 57 -84

nums = [int(num) for num in input().split()]
positive_numbers = [num for num in nums if num >= 0]
negative_numbers = [num for num in nums if num < 0]
sum_neg = sum(negative_numbers)
sum_pos = sum(positive_numbers)
print(sum_neg)
print(sum_pos)
if abs(sum_neg) > sum(positive_numbers):
    print(f'The negatives are stronger than the positives')
else:
    print(f'The positives are stronger than the negatives')