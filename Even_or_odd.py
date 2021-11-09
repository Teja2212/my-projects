even=0
odd=0
x=[2,4,55,67,84,88,96,1,90]
for i in range(len(x)):
    if x[i]%2==0:
        even+=1
    elif x[i]%2!=0:
        odd+=1
print("In the given set of array!! there are total")
print("Number of odd number is {0} and Number of even number is {1}".format(odd,even))
