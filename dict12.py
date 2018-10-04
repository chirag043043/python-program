list1=[('roll number',98),('name','raj'),('course','bcom')]
print(dict(list1))
print(end="")

dict={x:x*2 for x in range(1,11)}
print(dict)
print(dict[3])
dict['marks']=25
print(dict)
del(dict['marks'])
print(dict)
dict.clear()
print(dict)
del(dict)
print(dict)
