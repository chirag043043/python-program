import random
list1=[]
even=[]
odd=[]
for i in range(0,10):
    x=random.randrange(1,100)
    list1.append(x)
for i in list1:
    if(i%2==0):
     even.append(i)
    else:
     odd.append(i)
print("even number are",even)
print("odd number are",odd)
