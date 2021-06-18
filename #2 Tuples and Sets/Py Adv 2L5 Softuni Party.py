# Py Adv 2L5 Softuni Party - add/discard + sorting

# input / 5
# 7IK9Yo0h
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# tSzE5t0p
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# END
# output / 2
# 7IK9Yo0h
# tSzE5t0p

num = int(input())
reservation_nums = set()
for number in range(num):
    new_guests_arrived = input()
    reservation_nums.add(new_guests_arrived)

command = input()
while not command == "END":
    if command in reservation_nums:
        reservation_nums.discard(command)
    command = input()
print(len(reservation_nums))

sorted_nums = sorted(reservation_nums, key=lambda kvp: kvp[0])
for el in sorted_nums:
    print(el)