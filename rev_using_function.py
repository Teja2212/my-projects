def rev(s):
    newstr=""
    for i in s:
        newstr= i+ newstr
    return newstr
s= input("Enter a string ")
print("the reversed string is",rev(s))