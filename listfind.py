list1=[]
n=int(input("enter no of element"))
c=0
for i in range(0,n):
    a=int(input("enter element"))
    list1.append(a)
x=int(input("enter element to find"))
for i in range(0,n):
    if x==list1[i]:
        print("index=",i)
        c=c+1
    else:
        c=3
if x==3:
    print("element not in list")
else:
    print("count=",c)
    
    
