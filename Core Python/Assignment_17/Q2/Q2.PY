
class Student():
    def __init__(self,student_id = 0,student_name = " ",course = " "):
        self.id = student_id
        self.name = student_name
        self.course = course

    def accept(self):
        self.id = int(input("Enter id            : "))
        self.name = input("Enter name of student : ")
        self.course = input("Enter course        : ")
    

    def display(self):
        print("Student id     = ",self.id)
        print("Name Of Studnt = ",self.name)
        print("Course Of Student = ",self.course)
       

class EnggStudent(Student):
    def __init__(self, student_id=0, student_name=" ", course=" ",Branch = " ",InternalMark = 0):
        super().__init__(student_id, student_name, course)

        # self.Branch = Branch
        # self.InternalMark = InternalMark
    
    def accept(self):
        super().accept()
        self.Branch = input("Enter Branch: ")
        self.InternalMark = int(input("Enter internal mark: "))
        print("------------------------------------------")

    def display(self):
        super().display()

        print("Branch Of Student: ",self.Branch)
        print("InternalMark: ",self.InternalMark)
        print("--------------------------------")

E1 = EnggStudent()
E1.accept()
E1.display()


        



        