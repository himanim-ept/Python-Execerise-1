#Write a Python program to check whether a specified value is contained in a group of values.
#3 -> [1, 5, 8, 3] : True
#-1 -> [1, 5, 8, 3] : False

def is_check(value, n ):  # define method with value and n parameter
    if n in value:     # if n is also available in value
            return True # then its return true
    else:
     return False    # otherwise false

print(is_check([1,5,8,3] , 3)) # assign the value in method's parameter
