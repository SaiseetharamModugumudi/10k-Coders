#Sum of two digit number
n=479
s=0
while n>0:
    d=n%10
    s=s+d
    n=n//10
print(s)
#check a num even or odd
m=8
if n%2==0:
    print("Even")
else:
    print("Odd")    
#checking vowels in a string
def vow(st):
    v=['a','e','i','o','u']
    c=0
    for i in st.lower():
        if i in v:
            c+=1
    print(c)
vow('Sai')   
#checking palindrome
st="eye"
op=""
for i in range(len(st)-1,-1,-1):
    op+=st[i]
print(op)
if st==op:
    print(f"{st} is a palindrome")
else:
    print(f"{st} is not a palindrome") 
#find max num in list
list=[1,2,3,4,9,46,77]
maxm=max(list)
print(maxm)    
#revrse a string 
r="ram"
rev=""
for x in range(len(r)-1,-1,-1):
    rev+=r[x]
print(rev)
#print count repeated element
l=['a','b','b','c','c']
l2=[]
c=0
for i in l:
    if i not in l2:
        for j in l:
            if i==j:
                c+=1
        print(f"{i} appears {c} times")
        l2.append(i)
#FizzBuzz For numbers from 1 to N, print:
ip=int(input())
if ip%3==0 and ip%5==0:
    print("FizzBuzz")
elif ip%5==0:
    print("Buzz")  
elif ip%3==0:
    print("Fizz") 
else:
    print(f"Divisible by itself {ip}")
#