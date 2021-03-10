#Define a global dictionary. Define a function which takes 2 values 1st as key and 2nd as value.
# The function should add those key values to the global dictionary.

def func(d):
    for key in d:
        print("key:", key, "Value:", d[key])

    # Driver's code


D = {'a': 1, 'b': 2, 'c': 3}
func(D)