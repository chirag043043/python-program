a=[]
n=int(input("enter no of element"))
for i in range(0,n):
    b=int(input("enter element"))
    a.append(b)
for i in range(1,n-1):
    if(a[i]>a[i-1] and a[i]>a[i+1]):
        print(a[i],"and its index is",i)
