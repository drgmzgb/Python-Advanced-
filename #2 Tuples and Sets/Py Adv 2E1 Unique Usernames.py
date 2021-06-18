# Py Adv 2E1 Unique Usernames

#input
# 6
# George
# George
# George
# Peter
# George
# NiceGuy1234
# output
# George
# Peter
# NiceGuy1234
unique_names = set()
num = int(input())
for times in range(num):
    name = input()
    unique_names.add(name)
# {'George', 'Peter', 'NiceGuy1234'}
for el in unique_names:
    print(el)