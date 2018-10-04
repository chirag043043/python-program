values=[[3,4,5,1],[33,6,2,2]]   
v=values[0][0]
for list in values:
    for element in list:
        if v>element:
            v=element
print(v)
