# 1.check num is armstrong or not using 2nd approach(as discussed)
# 2.#find maximum num in the given list
# list=[4,7,1,2,8,9,10,1,3]
n=153
temp = n
sum = 0
digits = 0
t = n
while t > 0:
    digits += 1
    t >>= 1 
digits = len(str(n))
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp = temp // 10
if sum == n:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")

list=[4,7,1,2,8,9,10,1,3]
m=0
max=list[0]
for i in list:
    if i>max:
        max=i
print(max)        

n1 =5
if n1 & 1==0:
    print(f"{n1} is even")
else:
    print(f"{n1} is odd")    

n2=1364634685
conv=str(n2)
seq="02468"
if conv[-1] in seq:
    print("even")
else:
    print("odd")
    
