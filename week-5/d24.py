'''n=int(input("Enter a number: "))
temp=n
sum=0
digs=len(str(n))
while temp > 0:
    dig=temp % 10
    sum+=dig ** digs
    temp//=10
if sum==n:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")

 '''
dig=0
max=0
nums=4712591036
while nums>0:
    dig=nums%10
    if dig>max:
        max=dig
    nums=nums//10  
print(max)     

str="some"
i=0
dict={}
for i in range(0,len(str),1):
    dict[i]=str[i]
    i+=1
print(dict)    

str="sai"
x=0
dict2={}
for i in str:
    dict2[x]=i
    x+=1
print(dict2)  

str="ram"
x=0
dict1={}
while x<len(str):
    dict1[x+1]=str[x]
    x+=1
print(dict1)    