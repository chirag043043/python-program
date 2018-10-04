total=0
print("enter D or w  with amount")
t2=input("Enter String : ")
while t2!='exit':
    print("press exit to quit")
    t2=input("Enter String : ")
    var=t2.split()
    oper=var(0)
    amo=var(1)
    while total>0:
        if oper=='D' or oper=='d':
            total=total+amo
        else:
            total=total-amo
