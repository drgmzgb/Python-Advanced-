# Py Adv 4E2 Words Length - f string word+len of word and join print
# output Peter -> 5, George -> 6, Bill -> 4, Lilly -> 5, Katy -> 4
# input Peter, George, Bill, Lilly, Katy

res = [f'{word} -> {len(word)}' for word in input().split(", ")]
print(', '.join(res))

