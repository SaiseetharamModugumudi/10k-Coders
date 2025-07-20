# str="sai"
# rev=""
# for x in str:
#     rev=x+rev
# print("without indexing",rev)

# #with indexing
# print("with indexing",str[::-1])

# s="eye"
# s1=s[::-1]
# if s==s1:
#     print(f"{s} is palindrome")
# else:
#     print(f"{s} is not a palindrome")

# t="saiseetharam"
# cou=0
# vow="AEIOUaeiou"
# for y in t:
#     if y in vow:
#         cou+=1
# print(f"{t} have {cou} vowels")        

# nm="Sai Seetha Ram"
# cnt=""
# for x in nm:
#     if x ==" ":
#         continue
#     cnt+=x
# print("without method",cnt)    

# #with string method
# cnt1=nm.replace(" ","")
# print("with method",cnt1)

# st="im a software"
# coun=1
# for ch in st:
#     if ch==" ":
#         coun+=1
# print("no of words are",coun)        

# s = "aabbcdeff"
# freq = {}  
# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1
# for ch in s:
#     if freq[ch] == 1:
#         print("First non-repeated char:", ch)
#         break

# s = "tHiS iS swAPCAse"
# swapped = s.swapcase()
# print("Swapped case:", swapped)    

# l=[10,7,11,13,15,16]
# prm=True
# for x in l:
#     if x%2==0:
#         prm=False
#         continue
# if prm:
#     print("prime")
# else:
#     print("not a prime")            

# for i in range(len(l)):
#     if l[i]%2==0:
#         l[i]=l[i]+2
# print(l)

# l=['python',3.21,1234,True]
# for i in l:
#     if isinstance(i,str):
#         for x in range(len(i)):
#             if x%2==0:
#                 print(i[x])

# l=[10,7,11,13,15,16,12]
# l.sort()
# print(l[-1])

# res=l[0]
# for x in l:
#     if x>res:
#         res=x
# print(res)

# l=[1,3,5,7,8,43,33,5]
# d=list(l)
# a=list(d)
# print(a)

# s="Saiseetharam"
# h=set()
# for i in s:
#     h.add(i)
# print(h)

# s1={1,24,6,68,8}
# s2={46,8,9,3,2}
# print(s1|s2)
# print(s1&s1)
# print(s1-s2)

# h=[]
# n=int(input("no of students"))
# for i in range(0,n):
#     dic={}
#     dic['name']=input("Name")
#     dic['age']=input("Age")
#     dic['loc']=input("Location")
#     h.append(dic)
# print(h)

dict={}
s="pythoon"
for x in s:
    if x not in s:
        dict[x]=1 
else:
    dict[x]+=1
print(dict)        

# k={'a':10,'b':20,'c':30}
# sum=0
# for x in k.values():
#     sum+=x
# print(sum)    

# dic={}
# n=input("enter character")
# if n in "AEIOUaeiou":
#     print(n)
# else:
#     dic[n.upper()]=ord(n.upper())
#     print(dic)

# dics={}    
# a=['nam','age','city']
# b=['sai',22,'hyd']
# for i in range(len(a)):
#     dics[a[i]]=b[i]
# print(dics)        

# s=[1,2,3,4]
# res=[x*2 for x in s if x>0]
# print(res)

# n=10
# rs=[i for i in range(1,n) if n%i==0]
# print(rs)

# l=['python','java','c++']
# r=[len(x) for x in l]
# print(r)

# l1=[]
# es=['even' if x%2==0 else 'odd' for x in s]
# print(es)

