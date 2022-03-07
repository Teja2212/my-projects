#code by TEJANARASIMHA(09.01.2021)
n= int(input("Enter the size of array"))
lt=[]
count=0
for i in range(n):
    lt.append(int(input("enter element")))
lt.sort()
for i in range(1,n):
    if i<len(lt):
        j=i      
        if lt[j]-lt[i-1]==1:
            count+=1
            i+=1
if count==0:
    count=1
print(count)    