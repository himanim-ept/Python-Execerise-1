#Write a Python program to get the volume of a sphere with radius 15.
#Formula - 4/3 πr3
class volDemo: #create a class

   def volume():  #define the method
     r = 15       # assign the value to r
     formula = 4/3*(3.14*(r)) # formula for count the volume of sphere
     print("volume :",formula) # display the calculation of formula

p = volDemo  # create a class object
p.volume() #call the method