list1=[]
n=int(input("enter no of element"))
for i in range(0,n):
    a=int(input("enter element"))
    list1.append(a)
print(list1)
for i in range(0,n):
    for j in range(i+1,n-1):
        if(list1[i]==list1[j]):
            list1.remove(list1[j])
print(list1)
