#Py Adv WI 3 - Supermarket
customers = []
command = input()
while not command == "End":
    customers.append(command)
    if command == "Paid":
        customers.pop()
        for names in customers:
            print(names)
        customers = []

    command = input()
number = len(customers)
print(f"{number} people remaining.")