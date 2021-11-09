x=str(input("Enter a word "))
y=[0]*len(x)
l= len(x)-1
for i in range(len(x)):
    y[i]=x[l-i]
print("And the reversed string is:",end="  ")
for i in range(len(y)):
    print(y[i],end ="") 
print("") 




