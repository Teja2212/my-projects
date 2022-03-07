
class Employee:
    def __init__(self):
        self.emp_name=input("Enter the employye name:")
        self.emp_id=input("Enter employee id:")
        self.adress=input("Enter the adress")
        self.mail_id=input("Enter the mail_id:")
        self.mobile_no=input("Enter the mobile number:")
        
class programmer(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.bp=7500
        self.da=0.97*self.bp
        self.hra=0.1*self.bp
        self.pf=0.12*self.bp 
        self.club_fund=0.0001*self.bp
        self.tot=self.da+self.hra+self.pf+self.club_fund
    def pay(self):
        print("Programmer")
        print(self.tot)
class Associate_professor(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.bp=20000
        self.da=0.97*self.bp
        self.hra=0.1*self.bp
        self.pf=0.12*self.bp 
        self.club_fund=0.0001*self.bp
        self.tot=self.da+self.hra+self.pf+self.club_fund
    def pay(self):
        print("Associate_professor")
        print(self.tot)
class professor(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.bp=50000
        self.da=0.97*self.bp
        self.hra=0.1*self.bp
        self.pf=0.12*self.bp 
        self.club_fund=0.0001*self.bp
        self.tot=self.da+self.hra+self.pf+self.club_fund
    def pay(self):
        print("professor")
        print(self.tot)
a=professor()
b=Associate_professor()
c=programmer()
c.pay()
b.pay()
a.pay()