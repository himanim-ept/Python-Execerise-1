#Take 3 global dictionaries as follows.
# Define a function,which takes those 3 dictionaries and concatenate them.

dic1={1:10, 2:20} # create dictionary
dic2={3:30, 4:40}
dic3={5:50,6:60}

x = dic1.update(dic2) # concate the dictionary with update()
y = dic1.update(dic3)
print(dic1) # display the updated dic1