      
            
lt=[]



class cinema():
    def __init__(self,row,col):
        self.row=row
        self.col=col
        self.lt=[]
        for i in range(0,self.row+1):
            self.lt.append([])
            for j in range(0,self.col+1):
                self.lt[i].append(j)
                self.lt[i][j]=False
    def show_tickets(self):       
        for i in range(0,self.row+1):
            for j in range(0,self.col+1):
                if i==0and j==0 :
                    print(" ",end=" ")         
                elif i==0:
                    print("C{0}".format(j),end=" ")
                elif j==0:
                    print("R{0}".format(i),end=" ")
                else:
                    if self.lt[i][j]==False:
                        self.lt[i][j]="s"
                    elif self.lt[i][j]==True:
                        self.lt[i][j]="b"
                    print(self.lt[i][j],end="  ")
            print(" ")
    def booking_tickets(self,book_row,book_col):
        self.book_row=book_row
        self.book_col=book_col
        self.id=self.book_row*self.book_col
        conf=int(input("Do you want to continue?\n1.Yes\n2.No"))
        if conf==1:
            userdata={}
            userdata['Name']=input("Enter your name:")
            userdata['Gender']=input("Enter your gender:")
            userdata['mail']=input("Enter your e-mail")
            userdata['phone_number']=int(input("Enter your phone number"))
            if self.
            
        
        
ar= cinema(int(input("Enter the rows in theater")),int(input("Enter the columnsin the theater")))        
while True:
    choice=int(input("1.Show Tickets\n2.Book Tickets\n"))
    if choice==1:
        ar.show_tickets()
    elif choice==2:
        ar.booking_tickets(int(input("Enter the row number to book ")),int(input("Enter the column number to book")))
        
        
        
        
        