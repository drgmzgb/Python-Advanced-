# Py Adv WI L2 - Matching Parentheses

# input 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5
# output (2 + 3)
# (3 + 1)
# (2 - (2 + 3) * 4 / (3 + 1))

# expression = "1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5"
# expression = "(2 + 3) - (2 + 3)"
expression = input()
stack = []

for index in range(len(expression)):
    if expression[index] == "(":
        stack.append(index)
    elif expression[index] == ")":
        start_index = stack.pop()
        print(expression[start_index: index+1])