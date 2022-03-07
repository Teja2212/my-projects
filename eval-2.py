class times:
    def __init__(self):
        self.t1=list(map(int,input("Enter the Time1 in format HH:MM:SS : ").split(":")))
        self.t2=list(map(int,input("Enter the Time2 in format HH:MM:SS : ").split(":")))
        self.t3=[0,0,0]
    def add(self):
        self.t3[0]=self.t1[0]+self.t2[0]+(self.t1[1]+self.t2[1]+(self.t1[2]+self.t2[2])//60)//60
        self.t3[1]=(self.t1[1]+self.t2[1]+(self.t1[2]+self.t2[2])//60)%60
        self.t3[2]=(self.t1[2]+self.t2[2])%60
        return self.t3[0],self.t3[1],self.t3[2]
    def display(self):
        print("Total Timeis {0}:{1}:{2}".format(self.t3[0],self.t3[1],self.t3[2]))
t=times()
t.add()
t.display()