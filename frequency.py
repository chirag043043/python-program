t=input("Enter String : ")
print(t)
max = 0
p=0
t1=t.lower()
t2=t.isalpha()
for i in t2:
        if t2.count(i) > max:
            max = t2.count(i)
            p=i
print(p,end="")
print(" : ",max)
