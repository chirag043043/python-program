phonebal=int(input("Enter phone bal"))
bankbal=int(input("Enter bank bal"))
if(phonebal<10):
    bankbal-=50
    phonebal+=50
    print("phone bal is:- ", phonebal)
    print("bank bal is:-", bankbal)
else:
    print("phone bal is:- ", phonebal)
    print("bank bal is:-", bankbal)
