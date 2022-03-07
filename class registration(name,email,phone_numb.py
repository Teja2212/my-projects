#from final_project_edyodapri import veiwmenu
name=["a","b","c","d"]
price=[1,2,3,4]

class food_user():
    def __init__(self,name,email,phone_number,password,address):
        self.name=name
        self.email=email
        self.phone_number=phone_number
        self.password=password
        self.address=address
    def display_details(self):
        print("NAME:{0}".format(self.name))
        print("EMAIL:{0}".format(self.email))
        print("PHONE NUMBER:{0}".format(self.phone_number))
        print("PASSWORD:{0}".format(self.password))
        print("ADDRESS:{0}".format(self.address))
    def update_profile(self):
        self.name=input("Enter the new name")
        self.email=input("Enter the new email id")
        self.phone_number=input("Enter the new number")
        self.password=input("Enter the new password")
        self.address=input("Enter the new address")
    def printmenu(self):
        global name
        global price
        print("s.no\titem\tprice" )
        for i in range(len(name)):
            #self.items[i]=name[i]
            print("{0}\t{1}\t{2}".format(i+1,name[i],price[i]))
        self.arr=list(map(int,input("Enter the Item ID ").strip().split(",")))
        self.displaymainmenu()
        
    def orderhistroy(self):
        global price
        global name
        for i in range(len(self.arr)):
            print(name[self.arr[i]-1])
        
        
    def displaymainmenu(self):
        
        choice= int(input("1.Place New Order\n2.Order History\n3.Update Profile"))
        if choice==1:
            self.printmenu()
        elif choice==2:
            self.orderhistroy()
        elif choice==3:
            self.update_profile()
            print("The Details are updated")
        else:
            print("Enter a correct choice") 
            self.displaymainmenu()  
           
            
            
        
        
     
    

def create_user():
    n=input("Enter your name:") 
    e=input("Enter your valid email:")
    p=input("Enter Your 10 digit number:")
    pas=input("Enter your new password:")
    ad=input("Enter your city name:")
    new=food_user(n,e,p,pas,ad)
    new.display_details()
    new.displaymainmenu()
    
    
    
new1=create_user()


