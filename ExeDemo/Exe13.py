#Given variables x=30 and y=20, write a Python program to print "30+20=50".

def add(x,y):  #method with two parameter
    sum = x + y  # sum the varibles
    return sum

x = 10
y = 20
print(x,"+",y,"=",add(x,y))
#print("Key :", x, ",", "value is:", y)
print("'{}+{}={}'".format(x,y,add(x,y)))