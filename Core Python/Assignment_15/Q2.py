#2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowProduct

class product():
    def __init__(self,pid,pname,price,quantity):
        self.id = pid
        self.name = pname
        self.price = price
        self.quantity = quantity

    def showproduct(self):
        print("----------product details----------")
        print("product id:",self.id)
        print("product name:",self.name)
        print("product price:",self.price)
        print("product quantity: ",self.quantity)
        print("-------------------------------------")
    
    def __del__(self):
        print("distructor")

p1 = product(101,"derma facewash",399,"A1")
p1.showproduct()
p2 = product(102,"cetaphil facewash",499,"A1")
p2.showproduct()
