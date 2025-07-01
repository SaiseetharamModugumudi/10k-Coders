import math
list=[2.3,5.4,6.7,7.8,8.9,9.3]
for i in list:
    if i>5:
        op=math.ceil(i)
        print(op)
    else:
        op=math.floor(i)
        print(op)    

n=9.08
op=math.ceil(n)
op1=math.floor(n)
op2=math.trunc(-5.65) #it only return the sign integer vallu
print(op)
print(op1)
print(op2)


