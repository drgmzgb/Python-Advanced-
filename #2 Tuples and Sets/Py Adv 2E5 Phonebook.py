# Py Adv 2E5 Phonebook - dictionaries

# input Adam-0888080808
# 2
# Mery
# Adam
# output
# Contact Mery does not exist.
# Adam -> 0888080808
numbers = {}
while True:
    command = input()
    if not command.isdigit():
        name, number = command.split("-")
        numbers[name] = number
    elif command.isdigit():
        n = int(command)
        for _ in range(n):
            name_to_be_checked = input()
            if name_to_be_checked not in numbers:
                print(f"Contact {name_to_be_checked} does not exist.")
            else:
                for key, value in numbers.items():
                    if key == name_to_be_checked:
                        print(f"{name_to_be_checked} -> {value}")
        break
