lst=[1,2,3,4,5]
lst1=['word','letter','chararcter','sentence']
lst2=[]
todo_list=[]
for i in range(1,11):
    lst2.append(i)
print("list in reverse--------------------")
print(lst2[::-1])
temp=('hello','hii','byee')
lst4=list(temp)
print(lst4)
print("user input string-------------------")
#for i in range(5):
  #  do=input()
    #todo_list.append(do)
#print(todo_list)
print("concat many strings")
final=lst+lst1+lst2
print(final)
print("generating range based list-------------------")
lst5=list(range(10,40,3))
print(lst5)
print("max min in a list----------------")
print(max(lst5))
del(lst1[2])
print(lst1)
lst1.clear()
print(lst1)
lst1.append(40)
lst1.append(100)
print(lst1)
lst1.remove(100)
print(lst1)
print(lst2)
print(lst2.count(3))
x=lst2.copy()
print(x)
lst1.extend(lst5)
print(lst1)
