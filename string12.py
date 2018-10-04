str1="hello"
print("center()",str1.center(10, '*'))
print(min("hello"))
str2="this is a string.this is a string"
print(str2.replace( 'is', 'was',3))
str=input("enter a string")
count1=0
count2=0
for i in str:
      if(i.isdigit()):
            count1=count1+1
      elif(i.isalpha()):
            count2=count2+1
print("The number of digits is:")
print(count1)
print("The number of characters is:")
print(count2)


