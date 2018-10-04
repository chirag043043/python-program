a=input("enter a string")
for i in a:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        print(i,"is a vowel")
    elif(i==' '):
        continue
    else:
        print(i,"is a constonent")
