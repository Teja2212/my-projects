import re
def pass_check(passwd):
    	
	reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
	
	# compiling regex
	cmp = re.compile(reg)
	
	# searching regex				
	match = re.search(cmp, passwd)
	
	# validating conditions
	if match:
		print("Password is valid.")
	else:
		print("Password invalid !!")
  
# Definig a class food, 
# which contain name and price of the food item
def removeitem():
    id1=int(input("Enter the food id that is too be removed"))
    print(name[id1-1])
    del name[id1-1]
    del quantity[id1-1]
    del price[id1-1]
    return name,quantity,price
    

    

class Fooditem(object):
    def __init__(self, name, price,id_of_food,quantity):
        self.name = name
        self.price = price
        self.quantity=quantity
        self.id_of_food=id_of_food+1
    def removefooditem(self,id_of_food):
        '''self.name = []
        self.price = []'''
        self.quantity=0
        '''self.id_of_food=[]'''
        
        
    
    def getprice(self):
        return self.price
    
    def __str__(self):
        return  str(self.id_of_food) +':'+self.name + ' : ' + str(self.getprice())
  
# Defining a function for building a Menu 
# which generates list of Food    
def buildmenu(name,price,quantity):
    menu = []
    for i in range(len(name)):
        menu.append(Fooditem(name[i],price[i],i,quantity[i]))
    return menu
def veiwmenu():
    for el in Foodlist:
        print(el)
    

# items
name=["a","b","c"]
price=[1,2,3]
quantity=[11,12,13]
count=1
'''while count==1:
    name.append(input("Enter the dish name"))
    price.append(input("Enter the price of item"))
    quantity.append(input("Enter the quantity"))
    count=int(input("Do you want to add more\n press 1 or 0 to exit"))'''
#names = ['Coffee', 'Tea', 'Pizza', 'Burger', 'Fries', 'Apple', 'Donut', 'Cake']

# prices
#costs = [250, 150, 180, 70, 65, 55, 120, 350]

# building food menu




username = 'ADMIN'
password = 'Pass@1234'

#login for admin/user
print("Welcome!!!")
input_us_or_admin= int(input("Enter \n'1' for login for admin \n '2' for login for new user\n"))

if input_us_or_admin==1:
  userInput = 'ADMIN' #input("Enter the ?\n")
  if userInput == username:
    a="Pass@1234"#input("Password?\n") 
    
    if a == password:
      print("Welcome! {0}".format(userInput))
      Foodlist = buildmenu(name,price,quantity)
      veiwmenu()
      removeitem()
      '''print(name)
      print(price)
      print(quantity)'''
      newlist=buildmenu(name,price,quantity)
      for el in newlist:
            print(el)
      
      
      
      
      
      
        
      
    else:
      print("That is the wrong password.")
  else:
      print("That is the wrong username.")



        
 



'''# Driver Code	
if __name__ == '__main__':
    	main()'''

    