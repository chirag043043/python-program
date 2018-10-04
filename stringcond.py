str=input("enter a string")
lenght=len(str)
print(lenght)
if(lenght<2):
    print("empty string")
elif(lenght==2):
    print(str*2)
else:
    print(str[:3],end="");print(str[lenght-2:lenght]);
