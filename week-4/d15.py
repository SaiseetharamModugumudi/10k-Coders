"""l=[23,25,28,34,35,38,39,40,42,108,112]
for i in l:
    if i%3==0:
        print(i)

a=["apple","mango","pineapple","watermelon","orange","blueberry","banana"]
for i in a:
    b=len(i)
    if b%2==0:
        print(i)

for i in a:
    if 'e' in i:
        print(i)

employee_details = [
    {'name': 'Mountika', 'salary': 29000, 'role': 'HR'},
    {'name': 'Sreeja', 'salary': 32000, 'role': 'Developer'},
    {'name': 'KiranKumar', 'salary': 35000, 'role': 'HR'},
    {'name': 'Rajesh', 'salary': 28000, 'role': 'Developer'},
    {'name': 'Anusha', 'salary': 31000, 'role': 'Tester'},
    {'name': 'Vikram', 'salary': 34000, 'role': 'Manager'},
    {'name': 'Trinath', 'salary': 30000, 'role': 'HR'}
]

for emp in employee_details:
    if emp['salary']>=30000 and emp['role']=='HR':
        print(emp)
    
vowels = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')
for emp in employee_details:
    if emp['name'].startswith(vowels) and emp['salary'] > 30000:
        print(emp['name'])  

str= "Saiseetharam"
for char in str:
    if(char=="e"):
        continue
    print(char) 

subs=31
d=1
while(d<=subs):
    print(d)
    d+=1   

n=int(input())
while n>0:
    if(n%2==0):
        print("Even number")
        

 str=["html","css","js","python","flask","sql"]
i=0
while i < len(str):
    if len(str[i])%2!=0:
        break
print("Even indexs")
while i<len(str[i])%2==0:
    i+=1
    continue
print(str[i])   
i+=1 
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
test_numbers = [1, 2, 3, 4, 5, 10, 11, 17, 20, 23]
results = {num: is_prime(num) for num in test_numbers}
print(results)
