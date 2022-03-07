class Internalmarks:
    
    def __init__(self):
        self.p1=int(input("Enter P1 marks: "))
        self.p2=int(input("Enter p2 marks: "))
        self.e1=int(input("Enter e1 marks: "))
        self.e2=int(input("Enter e2 marks: "))
        self.e3=int(input("Enter e3 marks: "))

    def dispplayInternal(self):
        print(f"Periodical 1: {self.p1}")
        print(f"Periodical 2: {self.p2}")
        print(f"Evaluation 1: {self.e1}")
        print(f"Evaluation 2: {self.e2}")
        print(f"Evaluation 3: {self.e3}")

class ExternalMarks:

    def __init__(self):
        self.endsem = int(input("Enter the online end semester marks: "))
        self.viva  = int(input("Enter the Viva marks: "))

    def displayExternal(self):
        print(f"Online end sem mark: {self.endsem}")
        print(f"Online viva mark: {self.viva}")
    
class Student:
    
    def __init__(self):
        self.name = input("Enter your name: ")
        self.roll = input("Enter your roll number: ")

    def displaystudent(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll}")

class GradeCalculation(Student,ExternalMarks,Internalmarks):

    def __init__(self):
        Student.__init__(self)
        ExternalMarks.__init__(self)
        Internalmarks.__init__(self)
        self.tf=0
        self.gr=''

    def gradeCalculation(self):
        self.tf = self.p1+self.p2+self.e1+self.e2+self.e3+self.endsem+self.viva
        if 91<=self.tf<=100:
            self.gr='A'
        elif 81<=self.tf<=90:
            self.gr='B'
        elif 61<=self.tf<=80:
            self.gr='P'
        if self.tf<=60:
            self.gr='F'
        
    
    def displayGrades(self):
        print(f"Total marks: {self.tf}")
        print(f"Grade: {self.gr}")

obj = GradeCalculation()
print("--"*60)
obj.displaystudent()
obj.dispplayInternal()
obj.displayExternal()
obj.gradeCalculation()
obj.displayGrades()