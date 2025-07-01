a=5
if(a<10):
    print("Yes, a is less than 10")
print("solved")    

csk=True
if(csk):
    print("CSK won the match")
else:
    print("CSK loss the match")    

def cricket(match,team):
    if(match):
        print(f"{match} Won the match")
    else:
        print(f"{match} loss the match")    
cricket("CSK",True)
cricket("RCB",False)        

#write fun to disply the login status
def login(email,passwd):
    if(email==True and passwd==True):
        print("Login successfully")
    else:
        print("Unsuccessfully logined")    
login(True,True)        

def login(email,passwd):
    if(email=="sai@gmail.com" and passwd=="S@123"):
        print("Login successfully")
    else:
        print("Unsuccessfully logined")    
email=input("Email:")
passwd=input("Password:")
login(email,passwd)  