'''def seat(rank):
    if(rank<=10000):
        print("Get seat in JNTUH")
    elif(rank>10000 and rank<=25000):
        print("Get seat in MallaReddy College")
    elif(rank>25000 and rank<=50000):
        print("Get seat in Sri indu Engineering College")
    elif(rank<=150000):
        print("Get any local College")      
    else:
        print("Buy Management seat")       
rank=int(input("Enter rank:"))  
seat(rank)       

def auth(log,role):
    if(log==True):
      if(role=="admin"):
         return "This is admin"
      else:
         return "This is User"   
    else:
       return "Go and Login Once"
role=input("Enter Login User:")           
print(auth(True,role)) 

def seat(qualfy,rank):
    if(qualfy==True):
         if(rank<=10000):
            print("Get seat in JNTUH")
         elif(rank>10000 and rank<=25000):
             print("Get seat in MallaReddy College")
         elif(rank>25000 and rank<=50000):
             print("Get seat in Sri indu Engineering College")
         elif(rank<=150000):
             print("Get any local College")      
         else:
             print("Buy Management seat")     
    else:
         print("Get join in B.Com or B.Sc")           
#qualfy=input("Status:") 
#rank=int(input("Enter rank:")) 
seat(True,50000)   

def dev(front,back,data):
    if(front==True and back==True and data==True):
        print("He is a Full Stack developer")
    elif(front==True):
        print("He is Frontend Developer")
    elif(back==True):
        print("He is Backend Developer")
    elif(data==True):
        print("He is a Database Developer")   
    else:
        print("Go and Join 10000 Coders")
dev(True,True,True)                
dev(True,False,False)

#grade calculator
def grade_score(marks):
    if(marks>=90):
        print("A grade")
    elif(marks>=80 and marks<=89):
        print("B grade")
    elif(marks>=70 and marks<=79):
        print("C grade")
    elif(marks>=60 and marks<=69):
        print("D grade")
    else:
        print("Failed")
marks=int(input("Enter marks:"))
grade_score(marks)              

def num_chk(n):
    if(n>0):
        if(n%2==0):
            print("Given Number is Even")
        else:
            print("Given number is odd")
    else:
        print("It is not a number")            
n=int(input("Enter number:"))
num_chk(n)        

def temp(t):
    if(t<=15):
        print("Cold")
    elif(t>15 and t<=25):
        print("Moderate")
    elif(t>25):
        print("Hot")
t=int(input("Enter celsius"))
temp(t) 

def age_cat(a):
    if(a>0 and a<=12):
        print("Child")
    elif(a>13 and a<=19):
        print("Teenager")
    elif(a>20 and a<=60):
        print("Adult")    
    elif(a>60):
        print("Seniors")
a=int(input("Enter age:"))  
age_cat(a)      

#Basic Calculator: Take two numbers
def calc(a,b,op):
    if(op=="+"):
        print(a+b)
    elif(op=="-"):
        print(a-b)
    elif(op=="*"):
        print(a*b)
    elif(op=="/"):
        print(a/b)
a=int(input("a:"))
b=int(input("b:")) 
op=input("Operation:")
calc(a,b,op)                   

def login(email,passwd):
    if(email=="sai@gmail.com" and passwd=="S@123"):
        print("Access granted")
    else:
        print("Access denied")    
email=input("Email:")
passwd=input("Password:")
login(email,passwd)  

#Triangle Type Identifier
def tri_typ(a,b,c):
     if a == b == c:
        return "Equilateral"
     elif a == b or b == c or a == c:
        return "Isosceles"
     else:
        return "Scalene"
s1 =int(input("first side:"))
s2 =int(input("second side:"))
s3 = int(input("third side:"))
print("Triangle:", tri_typ(s1,s2,s3))  '''


def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year = int(input("Enter a year: "))
if leap_year(year):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is Not a Leap Year")
