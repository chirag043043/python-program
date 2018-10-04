list1=[]
string1=input("Enter String To Be Encrypted")
for i in string1:
    list1.append(i)
list1[0]=chr(ord(list1[0])+3)
for i in range(len(list1)):
    if(list1[i]==' '):
        list1[i+1]=chr(ord(list1[i+1])+3)
string1=''
for i in list1:
    string1+=i
print(string1)
