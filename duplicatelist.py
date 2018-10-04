list=[]
list1=[]
n=int(input("Enter the number of inputs"))
for i in range (n):
    x=int(input("Enter your flower tag"))
    list.append(x)
for i in list:
    if i not in list1:
        list1.append(i)
print("Final Bouquet Tag is:",list1)
