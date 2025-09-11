#3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook

class shirt():
    def __init__(self,sid = 101,sname = "T-shart",type = "informal",price = 400,size = "small"):
        self.id = sid
        self.name = sname
        self.type = type
        self.size = size
        self.price = price

    def showshart(self):
        print("------------cloth center ---------------")
        print("id: ",self.id)
        print("name:",self.name)
        print("pricc:",self.price)
        print("size:",self.size)
        print("----------------------------------------")

    def __del__(self):
        print("((((((((((((((()))))))))))))))")

s1 = shirt()
s1.showshart()
       