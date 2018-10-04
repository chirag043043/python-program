import re
p=r"hi(de)*"
if re.search(p,"hidedede"):
    print("matched")
if re.search(p,"hi"):
    print("matched")
else:
    print("not found")
#str=input("enter a string")
#p=r"[aeiouAEIOU]"
#if(len(p)>0):
  #  print("vowel found")
#else:
  #  print("vowel  not found")
p=r"2{1,4}$"
if re.match(p,"4322"):
    print("matched 4322")

if re.match(p,"433"):
    print("matched 433")
if re.match(p,"22222"):
    print("matched 222222")
else:
    print("not found")
import re

