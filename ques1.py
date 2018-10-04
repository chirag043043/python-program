a=(input("enter a string"))
l=len(a)
for i in range(0,l):
    if i==0:
        print(a[i],end="")
    elif i%3!=0:
        print(a[i],end="")
