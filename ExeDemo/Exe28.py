#Define a global empty dictionary. Iterate from 1 till 10 and fill the dictionary
# with the key as the number and value as the square of that number.
#reference from google
d={}

def add_values(x,y):
    d[x]=y

a=1
while(a<10): # prints uptil 10 items
    x=eval(input("Enter key {}:".format(a)))
    y=eval(input("ENter values corr. to key : "))
    add_values(x,y)
    a+=1
for x,y in d.items():
    print("Key is <",x,"> and value is <",y,">")