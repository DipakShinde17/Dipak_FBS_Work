class Product:
    Discount_Amount = 10
    Marked_Price = 1500
    Selling_Price = 1200

    def __init__(self,pid = 1,pname=" ",price=" ",quantity = ""):
        self.id = pid
        self.name = pname
        self.price = price
        self.quantity = quantity

    def ShowProduct(self):
        print("ID : ",self.id)
        print("NAME : ",self.name)
        print("PRICE:",self.price)
        print("QUANTITY: ",self.quantity)

    def cal():

        Product.Marked_Price = (Product.Marked_Price - Product.Selling_Price) // 100
        print("discount: ",Product.Discount_Amount)

p1 = Product("101","mouse",1600,"a1")
p1.ShowProduct()

Product.cal()


        
        