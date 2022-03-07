n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
# for i in range(n):
#     a[i].append(int(input()))
print(a)
l=int(n/2)
new1=[[]]*l
for x in range(l):
    for i in range(n):
        for j in range(i,n):
            if a[i]==a[j]:
                new1[x][i].append(a[i])
                new1[x][i+1].append(a[j])
                break
print(new1)                          