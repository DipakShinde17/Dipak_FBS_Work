class college:
    def __init__(self,nm,age,cls,grade):
        self.name = nm
        self.age = age
        self.cls = cls
        self.grade = grade

    def add(self):
        print("NAME: ",self.name)
        print("AGE: ",self.age)
        print("CLASS: ",self.cls)
        print("GRADE: ",self.grade)

name = input("Enter name: ")
age = int(input("Age enter : "))
clas = input("Enter class: ")
grade = input("enter grade: ")


obj1 = college(name,age,clas,grade)
obj1.add()