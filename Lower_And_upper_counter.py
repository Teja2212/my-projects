def lowerCase(str):
    l=0
    for i in x:
        if i.islower():
            l=l+1
    return l
def upperCase(str):
    u=0
    for i in x:
        if i.isupper():
            
            u=u+1
    return u
    
x=input("Enter a Sentence")

l=0
u=0
print("The number of Lower case letter are",lowerCase(x))
print("The number of Upper case letter are",upperCase(x))