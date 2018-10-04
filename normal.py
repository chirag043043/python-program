for i in range(0,51):
    if(i%5==0 and i%3==0):
        print("fizz buzz")
    elif(i%3==0):
        print("fizz")
    elif(i%5==0):
        print("buzz")
    
    else:
        print(i)
print("--------------------------------------------------")
i = 0
First_Value = 0
Second_Value = 1
while(i <10):
           if(i <= 1):
                      Next = i
           else:
                      Next = First_Value + Second_Value
                      First_Value = Second_Value
                      Second_Value = Next
           print(Next)
           i = i + 1
print("--------------------------------------------------")
for i in range(0,3):
    for j in range(0,5):
        print("*",end="")
    for k in range(0,3):
        print("*")
