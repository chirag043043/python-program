dict={}
counter=0
str1='New to Python or choosing between Python 2 or Python 3 ? read Python 2 or Python 3'
for n in str1:
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
    counter=0
    print("frequency of",n,"is",j)
