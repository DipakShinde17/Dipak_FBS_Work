from MedicalStudent import MedicalStudent

class Student(MedicalStudent):
    def __init__(self, Roll=0, name="", add="",Specialization = "",MarksOfInternship = 0):
        super().__init__(Roll, name, add)

        self.speci = Specialization
        self.mark = MarksOfInternship
    
    def accept(self):
        super().accept()

        self.speci = input("Enter Specialization: ")
        self.mark = int(input("Enter Mark: "))

    def dispaly(self):
        super().dispaly()

        print("Specialization: ",self.speci)
        print("MarksOfInternship:  ",self.mark) 

s1 = Student()
s1.accept()
s1.dispaly()