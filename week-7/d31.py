# num = 1234
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10
# print(rev)  # Output: 4321

# num = 7
# is_prime = True
# if num < 2:
#     is_prime = False
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
# print(is_prime)  # Output: True

# num = 5
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
# print(fact)  # Output: 120

# s = 'madam'
# is_palindrome = True
# for i in range(len(s) // 2):
#     if s[i] != s[-(i + 1)]:
#         is_palindrome = False
#         break
# print(is_palindrome)  # Output: True

# num = 123
# total = 0
# while num > 0:
#     total += num % 10
#     num //= 10
# print(total)  # Output: 6

# n = 5
# a, b = 0, 1
# for _ in range(n):
#     print(a, end=' ')
#     a, b = b, a + b
# # Output: 0 1 1 2 3

# num = 153
# n = num
# power = len(str(num))
# result = 0
# while n > 0:
#     digit = n % 10
#     result += digit ** power
#     n //= 10
# print(result == num)  # Output: True

# s = 'hello'
# vowels = 'aeiouAEIOU'
# count = 0
# for ch in s:
#     if ch in vowels:
#         count += 1
# print(count)  # Output: 2

# lst = [10, 30, 50, 40]
# max_val = lst[0]
# for num in lst:
#     if num > max_val:
#         max_val = num
# print(max_val)  

# lst = [4, 2, 5, 1]
# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] > lst[j]:
#             lst[i], lst[j] = lst[j], lst[i]
# print(lst)  

# s1 = 'listen'
# s2 = 'silent'
# if sorted(s1) == sorted(s2):
#     print(True)
# else:
#     print(False)
# # Output: True

# s = 'aabbc'
# freq = {}
# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1
# print(freq)  # Output: {'a': 2, 'b': 2, 'c': 1}

# lst = [1, 2, 2, 3, 4, 4]
# unique = []
# for item in lst:
#     if item not in unique:
#         unique.append(item)
# print(unique)  # Output: [1, 2, 3, 4]

# lst = [1, 3, 4, 2]
# first = second = float('-inf')
# for num in lst:
#     if num > first:
#         second = first
#         first = num
#     elif first > num > second:
#         second = num
# print(second)  

# year=2020
# leap= False
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     leap = True
# print(leap)  

# k=[5,4,3]
# for x in range(len(k)):
#     for y in range(len(k)):
#         if k[x]<k[y]:
#             k[x],k[y]=k[y],k[x]
# print(k)            

# import random 
# for x in range(0,10):
#     dt=random.randint(6000000000,9999999999)
#     print(dt)

n = int(input("num: "))
if n < 2:
    print("Not a +ve number")
else:
    cou = 0
    for i in range(2, n):
        if n % i == 0:
            cou += 1
    if cou == 0:
        print("Prime")
    else:
        print("Not prime")

'''lambda :
    filter
    map
    reduce'''