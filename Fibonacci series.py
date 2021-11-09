x=0
y=1
z=50
if z==1:
    print(x)
else:
    print(x, y,end=",")
    
    for i in range(2,z):
        next_element =x+y
        x=y
        y=next_element
        print(next_element,end=",")