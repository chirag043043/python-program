def word_count(string):
    my_string=string.lower().split()
    my_dict={}
    for item in my_string:
          if item in my_dict:
                my_dict[item]+=1
    else:
          my_dict[item]=1
    return(my_dict)

def keywithmaxval(d):
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))]
string=input("enter a string")
dict1=word_count(string)
print(dict1)
max_occur=keywithmaxval(dict1)
print("char with ",max_occur)
