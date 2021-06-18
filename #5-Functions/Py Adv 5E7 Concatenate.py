# Py Adv 5E7 Concatenate
# Write a function called concatenate() that receives some strings,
# concatenates them, and returns the result.
# output SoftUniIsGreat!
def concatenate(*args):
    res = ["".join(x for x in args)]
    return "".join(res)

print(concatenate("Soft", "Uni", "Is", "Great", "!"))