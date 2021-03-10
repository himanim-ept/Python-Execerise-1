#Write a Python program to check if all values are the same in a dictionary.
#Original Dictionary:{'Cierra Vega': 23, 'Alden Cantrell': 23, 'Kierra Gentry': 23, 'Pierre Cox': 23}
#Check all are 23 in the dictionary.
#True
#Check all are 10 in the dictionary.
#False

dict={'Cierra Vega': 89, 'Alden Cantrell': 89, 'Kierra Gentry': 23, 'Pierre Cox': 23}
l=list(dict.values())

def check_values(): # function defined to check if all dictionary values are same or not
    for x in l:
        if(x!=l[0]): # comparing first value with all other values
            return False
    return True

print(check_values())