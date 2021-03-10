#Define a global dictionary.
# Iterate through it and print the key and value of it separately in the following format.
#Key is <key> and Value is <value>

DictionaryDemo ={                       # create a dictionary with 2 key
                    "Fname":"Himani",
                    "lname": "Maheta"

                }
for x,y in DictionaryDemo.items(): # separate a dictionary key and value
    print("Key is :", x ,",","value is:", y)
