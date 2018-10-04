arr1=[]
ele=1
while ele!=0:
    ele=int(input("enter array element"))
    arr1.append(ele)
p=arr1[0]
c=0
for index,i in enumerate(arr1):
    if(p==arr1[index]):
        c=c+1
    p=arr1[index]
print(c)
