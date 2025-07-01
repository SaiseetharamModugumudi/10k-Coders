'''#1
villan="Ram"
def tel():
    print("This is global scope",villan)
tel()    

#2
def hin():
    villan="Dutt"
    print("this is local scope",villan)
hin()

#3
def tam():
    lan="Raj"
    def kan():
        print("this is a local scope accesed in another function",lan)
    kan()
    print("this is local scope",lan)
tam()

#4
def fun(**args):
    print(args)
fun(name="SAI", name1="ram", name2="Seetha")  

x=10 #it is a global variable scopes a variable created outside a function and can be used by anyone
def show():
    x=5 
    print(x)#it prints the local value first x=5
show()
print(x) #it prints the global value x=10

def outer():
    x=10 #it is a local variable prints the local value of x=5 by calling the local inner() function
    def inner():
        print(x) 
    inner()    
outer() 

x="global"
def outer(): #it is a enclosed scope a variable that is eighter local or global but exist within a nested function
    x="outer"
    def inner():
        x="inner" 
    inner() 
    print("outer:",x) 
outer() 
print("global:",x) '''
