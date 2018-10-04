arr=[]
c=0
a=int(input("enter array size"))
if(a>=3):
    for i in range(0,a):
        ele=int(input("enter array element"))
        arr.append(ele)
    for i in range (0,a):
        if(arr[0] and arr[1]):
            if(arr[i]==arr[i-1]+arr[i-2]):
                c=c+1
    if(c==(a-2)):
        print("yes")
    else:
        print("no")
else:
    print("enter an appropiate size for lucas series")

