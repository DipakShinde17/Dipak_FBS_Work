class MedicalStudent():
    def __init__(self,Roll = 0,name = "",add = ""):
        self.roll = Roll
        self.name = name
        self.add = add

    def accept(self):

        self.roll = int(input("Enter Roll Number: "))
        self.name = input("Enter Name : ")
        self.add = input("Enter Address : ")

    def dispaly(self):
        print("----------------------------------")
        print("ROLL NUMBER: ",self.roll)
        print("NAME OF STUDENT : ",self.name)
        print("ADDRESS: ",self.add)

# m1 = MedicalStudent()
# m1.accept()
# m1.dispaly()

