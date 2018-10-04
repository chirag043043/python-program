a=[]
n=int(input("enter no of element"))
for i in range(0,n):
    b=int(input("enter element"))
    a.append(b)
max=-1
index=0
count=0
for i in range(0,n):
    if(a[i]>max):
        max=a[i]
        index=i;
for i in range(0,n):
    if(a[i]==max):
        count=count+1
if(count==1):
    print("max=",max)
else:
    print("index is",index)
