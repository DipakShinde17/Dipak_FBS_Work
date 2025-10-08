from abc import ABC,abstractmethod
class vehicles(ABC):
    def __init__(self,basic,extra):
    
        self.basic = basic
        self.extra = extra
    @abstractmethod
    def cal(self):
        pass

class two_wheeler(vehicles):
    def __init__(self, basic, extra):
        super().__init__(basic, extra)

    def cal(self):
        self.per = int(input('Enter Person : '))
        if self.per > 2:
            Total = self.basic + self.extra * self.per
        else:
            Total = self.basic
        return Total
    
class three_wheeler(vehicles):
    def __init__(self, basic, extra):
        super().__init__(basic, extra)

    def cal(self):
        self.per = int(input("Enter person :  "))
        if self.per > 3:
            Total = self.basic + self.extra * self.per
        else:
            Total = self.basic
        return Total
    
class four_wheeler(vehicles):
    def __init__(self, basic, extra):
        super().__init__(basic, extra)

    def cal(self):
        self.per = int(input("Enter person: "))
        if self.per > 4:
            Total = self.basic + self.extra * self.per
        else:
            Total = self.basic
        return Total
    
class six_wheeler(vehicles):
    def __init__(self, basic, extra):
        super().__init__(basic, extra)

    def cal(self):
        self.per = int(input("Enter person: "))
        if self.per > 6:
            Total = self.basic + self.extra * self.per
        else:
            Total = self.basic
        return Total

ch = 0
print("""please select choice: 
      1.two wheeler
      2.three_wheeler
      3.four wheeler
      4.six wheeler
      5.Exite""") 
        
ch = int(input("SELECT CHOICE: "))
while ch != 5:
    if ch == 1:
        t = two_wheeler(20,10)
        print("pay the toll : ",t.cal())
    if ch == 2:
        t1 = three_wheeler(30,20)
        print("pay the toll : ",t1.cal())
    if ch == 3:
        t2 = four_wheeler(40,40)
        print("pay the toll : ",t2.cal())
    if ch == 4:
        t3 = six_wheeler(60,100)
        print("pay the toll : ",t3.cal())
    if ch == 5:
        print("thank youuuuuuuuuuuuuuuuuuu")



       

   
    



 



