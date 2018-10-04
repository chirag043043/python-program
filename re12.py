import re
#string="she sells sea shells on the sea shore"
#pattern1="she"
#if re.match(pattern1,string):
   # print("match found")
#else:
    #print(pattern1,"not found")
#string="she sells sea shells on the sea shore"
#pattern1="sea"
#if re.search(pattern1,string):
#    print("match found")
#else:
  #  print(pattern1,"not found")
#subsitute
string="she sells sea shells on the sea shore"
pattern1="sea"
pat2="ocean"
new_string=re.sub(pattern1,pat2,string)
print(new_string)
pattern=r"[a-zA-Z]+\d+"
matches=re.findall(pattern,"VXI 2014,VDI @013,hji 2014,dfi2104,maruti suzuki")
for match in matches:
    print(match,end=" ")
new_string=input("enter a string")
pat1=r"['a'+'e'+'i'+'o'+'u']"


