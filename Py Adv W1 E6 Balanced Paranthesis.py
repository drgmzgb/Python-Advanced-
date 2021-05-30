# Py Adv W1 E6 Balanced Paranthesis 37% errors: a lot by softunis

# input {[()]}
# # output
# YES
check_lst = []
command = input()
command_sliced = []
command_sliced[:] = command
NotBalanced = True
# ['{', '[', '(', ')', ']', '}']
from collections import deque
characters = deque(command_sliced)
while not len(characters) <= 0:
    if len(command_sliced) > 1:
        current_character = characters.popleft()
        check_lst.append(current_character)
        if current_character == "(":
            next_char = characters[0]
            if next_char == ")":
                NotBalanced = False
        elif current_character == "{":
            next_char = characters[0]
            if next_char == "}":
                NotBalanced = False
        elif current_character == "[":
            next_char = characters[0]
            if next_char == "]":
                NotBalanced = False
    elif len(command_sliced) <= 1:
        break
if NotBalanced:
    print("NO")
else:
    print("YES")