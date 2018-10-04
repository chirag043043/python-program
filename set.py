str="hello world"
setword=set(str)
print(setword)
days={'mon','tues','wed','thur'}
print(days)
print(set(str.split()))
set1={}
set1=set()
for x in range(5):
    x=x+1
    set1.add(x)
print(x)
days.add("sun")
print(days)
num1={1,2,3,4,5,}
num2={7,8,6,8,9}
print(num1.isdisjoint(num2))
print(all(num1))
for i in enumerate(days):
    print(i,end=" ")
