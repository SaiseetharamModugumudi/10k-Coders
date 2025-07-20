# # 1
# l1=[1,2,3,4,5]
# l2=[6,7,5,4,3]
# l=[]
# for x in l1:
#     if x in l2:
#         l.append(x)
# print(l)            

# # 2
# n=[]
# for i in range(0,21):
#     if i%3==0 and i%5==0:
#         n.append(i)
# print(n)        

# # 3
# p=['apple','wow','red','eye','madam']
# r=[]
# for x in p:
#     if x==x[::-1]:
#         r.append(x)
# print(r)        

# # 4
# s="abc"
# asc=[]
# for x in s:
#     asc.append(ord(x))
# print(asc)    

# # 5
# t=['apple','blue','python']
# rev=[]
# for i in t:
#     rev.append(i[::-1])
# print(rev)    

# # 6
# num=[1,2,3,4,5,6,7,8,9,11,13,15]
# l3=[]
# for y in num:
#     if y>1:
#         prime=0
#         for x in range(2,y):
#             if y%x==0:
#                 prime+=1
#                 break
#         else:
#             l3.append(y)
# print(l3)                

# # 7
# d = {'a': 10, 'b': 5, 'c': 15}
# val=list(d.values())
# print("Max dict:",max(val))
# print("Min dict:",min(val))

# # 8
# nes=[[1, 2, 3],[4, 5, 6]]
# f=[]
# for s in nes:
#     for i in s:
#         f.append(i)
# print(f)        

# # 9
# import copy
# list1 = [[1, 2], [3, 4]]
# shallow = copy.copy(list1)
# shallow[0][0] = 100
# print('shallow')
# print("Original:", list1)     
# print("Shallow:", shallow)
# list2 = [[1, 2], [3, 4]]
# deep=copy.deepcopy(list2)
# deep[0][0]=100
# print("deep")
# print("original:",list2)
# print("Deep",deep)

# li=[23,45,2,13,45,55]
# dics={}
# for n in li:
#     rs=[x for x in range(1,n) if n%x==0]
#     dics[n]=x
# print(dics)    

# res=tuple((x for x in range(10)))
# for x in res:
#     if x%2==0:
        # print(x)
        # print(*res)
# print(type(res))       
 
# without comprehension
# p=['pyhton','java','C++'] 
# r=tuple(p)
# # print(r)
# for x in r:
#     if len(x)==3:
#         print(x)

# rs=tuple(x for x in p if len(x)==3)
# print(rs)

# re=[[1,2,3],[4,5,6],[7,8,9]]
# t=tuple(y for x in re for y in x if y%2==0)
# print(t)

# a=[1,2,3]
# b=[10,20,30]
# to=tuple((a[x]+b[x]) for x in range(len(a)))
# print(to)

# n=2
# ta=tuple(x*2 for x in range(1,11))
# print(ta)

# dict compreh
# a={'a':1,'b':2,'c':3,'d':4}
# e={k:v for k,v in a.items() if v%2==0}
# print(e)

# r={1,2,3,4,5,6}
# rs={x:('even' if x%2==0 else 'odd') for x in r}
# print(rs)

# ka="pyhton"
# o={x.upper():ord(x.upper()) for x in ka  }
# print(o)

# li={'even':[x for x in (1,11) if x%2==0],'odd':[x for x in (1,11) if x%2==1]}
# print(li)

# res={'developer', 'python', 'java'}
# d={x:len(x) for x in res}
# print(d)

# x = 5
# for i in range(2,x):
# 	if x%i!=0:
# 		print(x)
# n=10
# count=0
# for j in range(1,n+1):
# 	for i in range(1,n+1):
# 		if j%i==0:
# 			count=count+1
# 		if count==2:
# 			print(j)
			
# def prime(n):
# 	if n>=1:
# 		return False
# 	for i in range(2,n):
# 		if n%i==0:
# 			return False
# 	return True
# for i in range(10):
# 	if prime(i):
# 		print(i)
		
# n = 5
# fact = 1
# for i in range(2, n + 1):
#     fact *= i
# print(fact)
	
# n = 7
# a, b = 0, 1
# fib = []
# for _ in range(n):
#     fib.append(a)
#     a, b = b, a + b

# print(fib)

# words=["cat", "dog", "bat"]
# reverse_dict = {}
# for word in words:
#     reverse_dict[word] = word[::-1]
# print(reverse_dict)

# ascii={}
# for ch in range(ord('a'), ord('z') + 1):
#     ascii[chr(ch)] = ch
# print(ascii)

# num={}
# for i in range(1, 4):
#     num[i] = {'square': i ** 2,'cube': i ** 3, '4times':i**4}
# print(num)

# traf=input("enter color")
# if traf=="red":
#     print("Stop")
# elif traf=="yellow":
#     print("Ready")
# elif traf=="green":
#     print("Move")
# else:
#     print("trafic light problem")            

# usr=input("Enter Usrname:")
# pas=input("Enter passwd:")
# if usr=="Sai":
#     if pas=="S@123":
#           print("Login Successfull")
#     else:
#            print("Login failed pls check the credintials")  
# else:
#     print("check usrname")          

# n=2
# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")
    
# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)    

# n=5
# a,b=0,1
# for i in range(0,n):
#     a,b=b,a+b
#     print(a)

# l=[[1,2,3],[4,5,6],[7,8,9]]
# l1=[]
# for x in l:
#     l1=l[0]+l[1]+l[2]
# print(l1)    
# print(max(l1))

for x in range(5,10):
    for y in range(1,11):
        print(f"{x} X {y} = {x*y}")
    print()     