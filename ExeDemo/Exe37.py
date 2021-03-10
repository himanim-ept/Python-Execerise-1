# Write a program having classes as Product, Order, Customer
# Do appropriate inheritance of the above classes
# Write appropriate methods / constructors in each classes
# Following output is expected
# Order No : SO001
# Customer : Sanjay Patel
# Customer Email : sanjay@dummy.com
# Name of the product is 'Pencil'
# Product Qty is : 15
# Unit Price is 20
# Order total is : 300

class Product :
    def __init__(self,Product_Name):
        self.Product_Name = Product_Name
    def fun(self):
        print("Product Name:",self.Product_Name)

class Customer :
    def __init__(self,Customer_Name,Customer_Email):
        self.Customer_Name = Customer_Name
        self.Customer_Email = Customer_Email

    def cusFun(self):
        print("Customer Name :",self.Customer_Name)
        print("Customer Email :",self.Customer_Email)


class Order(Product,Customer):
    def __init__(self,Order_no,Customer_Name,Customer_Email,Product_Name,Product_Qty,Unit_Price):
        Product.__init__(self,Product_Name)
        Customer.__init__(self,Customer_Name,Customer_Email)
        self.Order_no = Order_no
        self.Product_Qty = Product_Qty
        self.Unit_Price = Unit_Price

    def Ordfun(self):
     print("Order no :",self.Order_no,"\nProduct Qty:",self.Product_Qty,"\n Unit Price:",self.Unit_Price)
     print("Customer Name :", self.Customer_Name,"\nCustomer Email:",self.Customer_Email)
     print("Product Name :",self.Product_Name)
     print("Order Total : ", self.Product_Qty * self.Unit_Price)


OrObj = Order('S002','Himani','himanimaheta25@gmail.com','Pencil',15,10)
print(OrObj.Ordfun())