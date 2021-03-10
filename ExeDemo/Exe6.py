#Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return three times of their sum.

number1 =int( input("enter the number1 :")) # enter these number from user
number2 = int(input("enter the number2 :"))
number3 = int(input("enter the number3 :"))
def add(number1,number2,number3):  # method with above number parameter

    sum = number1 + number2 + number3 # store the calculation of the number n sum
    if number1==number2== number3:  # if the all entered no. is same
        sum = sum * 3 # then its sum multiply by 3
        return sum    # display the sum
    else:
        return sum

print (add(number1,number2,number3))