#Write a Python program which accepts a sequence of comma-separated numbers from the user
# and generates a list and a tuple with those numbers.
#Sample data : 3, 5, 7, 23
#Output :
#List : ['3', ' 5', ' 7', ' 23']
#Tuple : ('3', ' 5', ' 7', ' 23')



values = input(" Enter the Number : ")  #get the input vales from user
list = values.split(",") # splits a string into a list
tuple = tuple(list)  # tuple contain the list value
print('List : ',list)  #display list in output
print('Tuple : ',tuple) #dispaly tuple in output