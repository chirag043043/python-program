n=int(input("enter"))
count=0
for i in range (0,n):
      a=input("enter string")
      b=len(a)
      if(b>=2):
            count=count+1
      if(a[0]==a[b-1]):
            print(a)
print (count)
