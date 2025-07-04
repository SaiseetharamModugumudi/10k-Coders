# x=["s","a","i","s","e","e","t","h","a","r"]
# d={}
# i=0
# for i in x:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

# dic={"emp1":25000,"emp2":20000,"emp3":30000}
# sum=0
# for i in dic:
#     sum+=dic[i]
# print(sum)    

# # dict={"st1":"sai","st2":"ram","st3":"reddy","st4":"seetha"}
# # srch=input("search name: ")
# # for x in dict:
# #     if dict[x]==srch:
# #         print(f"{srch} name found")
# #         break
# #     else:
# #         print("Not found")

# dics={"a":10,"b":15,"c":20,"d":17}
# dicu={"e":14,"b":25,"d":13,"f":30}
# dicv={}
# for i in dics:
#    dicv[i]=dics[i]
# for i in dicu:
#     if i in dicv:
#        dicv[i]+=dicu[i] 
#     else:
#        dicv[i]=dicu[i]   
# print(dicv)               

# dict1 = {"x": 2, "y": 4, "z": 8}
# inv = {}
# for key in dict1:
#     val = dict1[key]
#     inv[val] = key
# print(inv)
   
#sunny number
# n=int(input("n:"))
# num=n+1
# i=1
# psq=False
# while i<=num:
#     if i*i==num:
#         psq=True
#         break
#     i+=1    
# if psq:
#     print(f"{n} is a sunny number")
# else:
#     print(f"{n} is not a sunny")    

# #Neon number
# n1=int(input("n1:"))
# sn = n1 ** 2
# s = 0
# while sn > 0:
#     ld = sn % 10
#     s += ld
#     sn //= 10
# print(f"sum of digits: {s}")
# if s == n1:
#     print(f"{n1} is Neon num")
# else:
#     print(f"{n1} is Not neon num")
   
# n=10
# for i in range(n):
#     sq=i*i
#     print(sq)    

    

# f1,f2,f3,*res,f4=["apple","banana","grapes","mango","orange","pineapple","kiwi","lichi","dragon fruit"]
# print(f1)
# print(f2,f3)
# print(res)
# print(f4)

# n=2
# count=0
# while count>5:
#     sdiv=0
#     for i in range(1,n):
#         if n%i==0:
#             print(i)
#             sdiv+=i
#     if sdiv==n:
#         print(n,end=" ")
#         count+=1
#     n+=1

# count = 0
# num = 2
# while count < 5:
#     sum_div = 0
#     for i in range(1, num):
#         if num % i == 0:
#             sum_div += i
#     if sum_div == num:
#         print(num, end=' ')
#         count += 1
#     num += 1    

# a,b,*c=(1,2,3,4,5)
# print(a,b,c)

# x="sai"
# print(hash(x))

# l,m,n,o={"Dell","Hp","Mac","Lenovo"}
# print(l,m,n,o)

# dict={"nam":"sai","age":22,"bld":"A+"}
# d,*e=dict
# print(d,dict[d])
# print(e)

# a=[1,2,3,4,5]
# b=[5,6,7,8]
# c=["s","a","i"]
# d={"nam":"ram","age":22}
# mg=[*a,*b,*c,*d]
# print(mg)

# dic1={"k1":"sai"}
# dic2={"k2":"ram"}

# list=["Sai","ram","SEETHA","hi"]
# op=[x.upper() for x in list if len(x)<=3]
# print(op)

# def prime(x):
#     if x/2==1:
#         return True
# l=[x for x in range(1,10) if prime(x)]
# print(l)

# l=[x**2 for x in range(1,6) ]
# print(l)

# list=[1,4,8,34,88]
# l1=[x+x for x in list]
# print(l1)

# list1=["sai","RAM"]
# # l2=[e=len(x) for x in list1]
# # print(l2)

# l3=[x for x in range(list1(::-1))]
# print(l3)

# def fact(n):
#     f=1
#     for x in range(1,n+1):
#         f=f*x
#     return f
# def pnum(f,num):
    
# def prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(**0.5)+ 1):
#         if n % i == 0:
#             return False
#     return True
# op = [i for i in range(10, 30) if prime(i)]
# print(op)

# ip=["sai","ram","seetha"]
# str=""
# for x in ip:
#     for y in range(len(x)-1,-1,-1):
#         str=x[y]
#     print(str)

# num=[4234,345,234]
# rev=0
# for z in num:
#     while z>0:
#         ld=z%10
#         rev=rev*10+ld
#         z=z//10
# print(rev,end=" ")    

# x=["AB","ab"]
# for i in x[0]:
#     for j in x[1]:
#         print(i+j)

st=["HeLlo","Sai","RaM"]
cvtr=""
for y in st:
    for x in y:
        if x==x.upper():
            cvtr+=x.lower()
        else:
            cvtr+=x.upper()    
print(cvtr)        
