import re
'''def pass_check(passwd):
    	
	reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
	
	# compiling regex
	cmp = re.compile(reg)
	
	# searching regex				
	match = re.search(cmp, passwd)
	
	# validating conditions
	if match:
		print("Password is valid.")
	else:
		print("Password invalid !!")'''
'''class registration():
    def __init__(self,name,email,phone_number,password,address):
        self.name=name
        self.email=email
        self.phone_number=phone_number
        self.password=password
        self.address=address
    def display_details(self):
        print(self.name,self.email,self.phone_number)
def create_user():
    n=input("Enter your name") 
    e=input("Enter your valid email")
    p=input("Enter Your 10 digit number")
    pas=input("Enter your new password")
    ad=input("Enter your city name")
    registration(n,e,p,pas,ad)'''
    
# Definig a class food, 
# which contain name and price of the food item
name = ['Coffee', 'Tea', 'Pizza', 'Burger', 'Fries', 'Apple', 'Donut', 'Cake']

price = [250, 150, 180, 70, 65, 55, 120, 350]
def removeitem():
    id1=int(input("Enter the food id that is too be removed"))
    print(name[id1-1])
    del name[id1-1]
    del quantity[id1-1]
    del price[id1-1]
    return name,quantity,price
def stockupdate():
    for i in range(len(stock)):
        stock[i]=stock[i]-[i] 
    return stock 

    

class Fooditem(object):
    def __init__(self, name, price,id_of_food,quantity):
        self.name = name
        self.price = price
        self.quantity=quantity
        self.id_of_food=id_of_food+1
    '''def removefooditem(self,id_of_food):
        self.name = []
        self.price = []
        self.quantity=0
        self.id_of_food=[]'''
        
    def getprice(self):
        return self.price
    
    def __str__(self):
        return  str(self.id_of_food) +':'+self.name + ' : ' + str(self.getprice())
  
  
def buildmenu(name,price,quantity):
    menu = []
    for i in range(len(name)):
        menu.append(Fooditem(name[i],price[i],i,quantity[i]))
    return menu
def veiwmenu():
    for el in Foodlist:
        print(el)
    

# items
#name=["a","b","c","d"]
#price=[1,2,3,4]
quantity=[4,4,250,200]
#1. Tandoori Chicken (4 pieces) [INR 240]
#2. Vegan Burger (1 Piece) [INR 320]
#3. Truffle Cake (500gm) [INR 900]
#4. lime juice(250ml)[inr250]
stock =[20,20,50000,20000]
count=1
'''while count==1:
    name.append(input("Enter the dish name"))
    price.append(input("Enter the price of item"))
    quantity.append(input("Enter the quantity"))
    count=int(input("Do you want to add more\n press 1 or 0 to exit"))'''


# building food menu
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
        self.displaymainmenu()
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
        print("Your order hasbeen placed succesfully")
        
        
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
def admin_menu():
    nw=int(input("1.veiw menu\n2.removeitems"))
    if nw==1:
        newlist=buildmenu(name,price,quantity)
        for el in newlist:
            print(el)
        #admin_menu()
        back()
    elif nw==2:
        removeitem()
        updatedlist=buildmenu(name,price,quantity)
        for el in updatedlist:
            print(el)
        #admin_menu()
        back()
def back():
    xy=int(input("If you want to go back enter 1 or for stay here enter 2"))
    if xy==1:
        run()
    elif xy==2:
        admin_menu()    
    
    




username = 'ADMIN'
password = 'Pass@1234'
def run():
    print("Welcome!!!")
    input_us_or_admin= int(input("Enter \n'1' for login for admin \n'2' for login for new user\n"))

    if input_us_or_admin==1:
        userInput =  input("Enter the user id for admin(TYPE 'ADMIN') ?\n")
        if userInput == username:
            a=input("Password? (TYPE'Pass@1234)\n") 
    
            if a == password:
                print("Welcome! {0}".format(userInput))
                Foodlist = buildmenu(name,price,quantity)
                for el in Foodlist:
                    print(el)
                rm=int(input("Do you want remove any item press 1"))
                if rm==1:
                    removeitem()
                
                    
                
                newlist=buildmenu(name,price,quantity)
                for el in newlist:
                    print(el)
                print("Do You want to switch to user?")
                us=int(input("Enter 1 for swtiching 2 for wants to change the menu"))
                if us==1:
                    run()
                elif us==2:
                    
                    
                            
                    admin_menu()   
                        
                    
                    
     
            else:
                print("That is the wrong password.")
                run()
                
        else:
            print("That is the wrong username.")
            run()
    elif input_us_or_admin==2:
        print("HELLO NEW USER")
        new1=create_user()
    else:
        print("INVALID INPUT")
        run()
    
run()    

#login for admin/user



        
 






        
     
    



