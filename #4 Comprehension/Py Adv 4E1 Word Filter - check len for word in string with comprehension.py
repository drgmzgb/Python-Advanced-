# Py Adv 4E1 Word Filter - check len for word in string with comprehension
# output kiwi
# orange
# banana
# intput kiwi
# orange
# banana

res = [word for word in input().split() if len(word) % 2 == 0]
for word in res:
    print(word)