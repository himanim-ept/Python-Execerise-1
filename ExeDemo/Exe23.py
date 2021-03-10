#Write a Python program to multiply all the items in a list.

list = [4,5,7,9,3]

def multiply(mul):
    value = 1     #give a static value
    for i in mul:
        value= value*i  #multiply with static value
    return value
print(multiply(list))