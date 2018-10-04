digit=int(input("enter the no"))
sum=0
num=0
while digit>0:
    num=digit%10
    sum+=num
    digit//=10
print(sum)
