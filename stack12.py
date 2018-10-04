a=[]
n=int(input("enter how many number to insert"))
for i in range(0,n):
        j=int(input())
        a.append(j)
choice=int(input("enter choice"))
while(choice!=-1):
    if(choice==1):
        print("enter number to insert")
        h=int(input())
        a.append(h)
        print(a)
    elif(choice==2):
        a.pop()
        print(a)
    else:
        print(a)
    choice=int(input())
