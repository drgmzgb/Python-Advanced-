# Py Adv 5E6 arguments length
# Create a function called args_length()
# that returns the number of the arguments.
# Submit only the function in the judge system.
# print(args_length(1, 32, 5))
# output 3
def args_length(*args):
    return len(args)

result = print(args_length(1, 32, 5))