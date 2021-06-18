# Py Adv 5E35 odd or even
# output 490
# input Odd
# 1 3 5 34 7 9 12 11 13 10
command = input()
nums = [int(num) for num in input().split()]
odd_nums = [num for num in nums if not num % 2 == 0]
even_nums = [num for num in nums if num % 2 == 0]
if command == "Odd":
    res = sum(odd_nums) * len(nums)
elif command == "Even":
    res = sum(even_nums) * len(nums)
print(res)