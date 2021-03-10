# Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Don’t use static value for 11-20, 21-30, 31-40. Access the fifth value of each key from the dictionary.
# Expected Output
# First
# x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
# y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
# z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]
# Second
# 15
# 25
# 35

dict={'x':[11,12,13,14,15,16,17,18,19,20],'y':[21,22,23,24,25,26,27,28,29,30],'z':[31,32,33,34,35,36,37,38,39,40]}

def display_val():
    for x,y in dict.items():
        print(x," has values ",y)

    for y in dict.values():
        print(y[4])

display_val()
