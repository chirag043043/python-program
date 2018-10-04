a=int(input("Enter Number : "))
c=0
rem=0
b=0
d=a
f=0
while(a>0):
    c=c+1
    rem=a%10
    f=rem+f
    a=a//10
    b=rem+10*b

if(d==b):
    print(f)
else:
    print(c)
