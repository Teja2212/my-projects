def sum(x):
    s=0
    for i in range(len(x)):
        s=s+x[i]
    return s
y=int(input("enter the length of list"))
x=[0]*y
for i in range(y):
    x[i]=int(input("Enter the number"))
print("The total number of sum is :",sum(x))