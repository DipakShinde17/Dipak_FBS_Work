class Shirt:
    base_price = 1000
    def __init__(self,sid,sname,type, size):
        self.id = sid
        self.name = sname
        self.type = type
        self.size = size

        self.price = Shirt.cal(size)
      
    @staticmethod
    def cal(size):
        
        if size == "small":
            return Shirt.base_price
        elif size =="medium":
            return Shirt.base_price*1.1
        elif size == "large":
            return Shirt.base_price*1.2
        elif size == "Xlarge":
            return Shirt.base_price*1.3
        else:
            return Shirt.base_price*1.3
 
        
    def show(self):
        print(f"size {self.size},price:",self.price)

    def Showbook(self):
        print("---------------------------------------")
        print("ID : ",self.id)
        print("NAME: ",self.name)
        print("TYPE : ",self.type)
        print("SIZE: ",self.size)
        print("PRICE: ",self.price)
    
    def distructor(self):
        print("distructor call")

s1 = Shirt(101,"t-shart","informal" ,"small")
s2 = Shirt(102,"t-shart","informal" ,"medium")
s3 = Shirt(103,"t-shart","informal" ,"large")
s4 = Shirt(104,"t-shart","informal" ,"xlarge")

s1.show()
s2.show()
s3.show()
s4.show()

s1.Showbook()
s2.Showbook()
s3.Showbook()
s4.Showbook()

s1.distructor()

    

    
    
    