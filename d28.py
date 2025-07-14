# reverse triangle
for l in range(5,0,-1):
    t=""
    for m in range(l):
        t+="x"
    print(t)

# 55555
# 4444
# 333
# 22
# 1
for i in range(5,0,-1):
    result =0
    for j in range(i):
        result = result*10+i
    print(result)

# 54321
# 5432
# 543
# 54
# 5
for i in range(5,0,-1):
    result =0
    for j in range(5,5-i,-1):
        result = result*10+j
    print(result)

# abcdef
# abcde
# abcd
# abc
# ab
# a
l = "abcdef"
for i in range(6,0,-1):
    result = ""
    for j in range(i):
        result+= l[j]
    print(result)

# fabcde
# fabcd
# fabc
# fab
# fa
# f
l = "abcdef"
for i in range(6,0,-1):
    result = ""
    for j in range(i):
        result+= l[j-1]
    print(result)

# ffffff
# eeeee
# dddd
# ccc
# bb
# a
l = "abcdef"
for i in range(6,0,-1):
    result = ""
    for j in range(0,i):
        result+=l[i-1]
    print(result)

# aaaaaa
# bbbbb
# cccc
# ddd
# ee
# f
l = "abcdef"
for i in range(len(l)):
    result = ""
    for j in range(len(l),i,-1):
        result+=l[i]
    print(result)

# n=5
# for i in range(1,11):
#     print(f'{n} x {i} = {n*i}')

# n=123
# sum=0
# for i in range(0,n):
#     ld=n%10
#     sum+=ld
#     n=n//10
# print(sum)    

# n=123
# for i in range(0,n):
    