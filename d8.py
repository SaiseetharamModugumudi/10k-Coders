def movie(mname,tic_price,quan,gst=0.05):
    tot_price=quan*tic_price*gst + tic_price*quan
    return f"total amount is {tot_price}, watch and enjoy movie {mname}"
x=movie("RRR",150,5)
print(x)

def family(*kids):
    print(kids[0])
family("sai","ram","seetha")    

a=input("enter a value")
print(a)

def demo():
    return "hello"
print(demo())

#student details function
def stud(name,age,gender,qualification):
    return f" Name:{name} \n Age:{age} \n Gender:{gender} \n Qualification:{qualification}"
print(stud("Sai Seetharam",21,"Male","B.tech"))
print("\n")

#favorite food items
def food_list(*items):
    print(items)
food_list("Chicken","Biryani","Mutton")  
print("\n")

#travel bus information
def travel(psgname,fromto,to,buspartner="AbhuBus"):
    return f"Hello Passenger {psgname} greeting from {buspartner} .Your journey from {fromto} to {to} is confirmed. Happy Journey."
print(travel("Sai","HYD","MTM"))
print("\n")
