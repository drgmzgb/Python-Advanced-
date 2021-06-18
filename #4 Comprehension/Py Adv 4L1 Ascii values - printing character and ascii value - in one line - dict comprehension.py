# Py Adv 4L1 Ascii values - printing character and ascii value - in one line - dict comprehension
# output {'a': 97, 'b': 98, 'c': 99}
# input a, b, c, a

result = print({char: ord(char) for char in input().split(", ")})
