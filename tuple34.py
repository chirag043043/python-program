nestup=(("aarav","btech",9),
        ("neha","bcom",98),
        ("chir","bba",99))
newtup=()
for i in nestup:
      print(i)
n=input("DO YOU WANT TO  EDIT")
if n=='y':
      name=input("enter name of student")
      new_n=input("new name")
      new_c=input("new course")
      new_m=input("new marks")
      for i in range(len(nestup)):
          if nestup[i][0]==name:
              newtup +=(new_n,new_c,new_m)
          else:
              newtup+=nestup[i]
      print(newtup)
else:
    print("thanks")
