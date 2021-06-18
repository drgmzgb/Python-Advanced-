# Py Adv 2E3 Periodic Table - set add

# input 4
# Ce O
# Mo O Ce
# Ee
# Mo
# output Ce
# Ee
# Mo
# O
periodic_table = set()
n = int(input())
for num in range(n):
    command = input().split()
    for el in command:
        periodic_table.add(el)
# {'Ce', 'Ee', 'O', 'Mo'}

for element in periodic_table:
    print(element)

