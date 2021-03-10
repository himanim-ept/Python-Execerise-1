#Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference.

def difference(k):  #define the Method
    if k >17:
       return (k-17)*2 # if the below condition is true then its return these calculation
    else:
        return 17-k # if false then return these
print(difference(20)) # assign the value to method
print(difference(16))