# L1 Reverse string
#input I Love Python
#output nohtyP evoL I
reversed_res = []
text = input()
text_characters = []
text_characters[:] = text
# ['I', ' ', 'L', 'o', 'v', 'e', ' ', 'P', 'y', 't', 'h', 'o', 'n']
while not len(text_characters) <= 0:
    res = text_characters.pop()
    reversed_res.append(res)
print("".join(reversed_res))