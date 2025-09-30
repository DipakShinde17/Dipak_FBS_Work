class Student():
    def __init__(self,studentID=0 ,name="jj",age=0,Gain_mark=9):
        self.id = studentID
        self.name = name
        self.age = age
        self.per = Gain_mark


    def accept(self):

      self.id = int(input("Enter id : "))
      self.name = input("Enter name :")
      self.age= int(input("Enter age: "))
    #   self.per= float(input("Enter percentage: "))
      self.Gain_mark  = int(input("Enter mark: "))

    def display(self):

        print("Student_Id: ",self.id)
        print("Name: ",self.name)
        print("Age: ",self.age)
        # print("Percentage: ",self.per)

    def calculate(self):

        percentage= (self.Gain_mark/500)*100

        print("percentage of 5 mark: ",percentage)

        
        if(percentage>= 90):
            print("Grade: A++")
        elif(percentage >= 75):
            print("Grade: A")
        elif(percentage>= 50):
            print("Grade: B++")
        elif(percentage>= 35):
            print("Grade: B")

S1 = Student()
S1.accept()
S1.display()
S1.calculate()


    