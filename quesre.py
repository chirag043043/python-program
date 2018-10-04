import re
string=input("enter a string")
pattern=r"^a[a-zA-Z]*b$"
if re.search(pattern,string):
    print("match found")
else:
    print("not found")
string=input("enter a string for ques 2")
pattern1=r"[aA][bB]*"
if re.search(pattern1,string):
    print("match found")
else:
    print("not found")
string=input("enter a string for ques 3")
pattern1=r"[aA][bB]+"
if re.search(pattern1,string):
    print("match found")
else:
    print("not found")
