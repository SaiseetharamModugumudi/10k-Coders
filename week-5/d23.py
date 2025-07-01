''' str="saiseetharam"
c=0
l=input()
for ch in str:
    if ch==l:
        c+=1
print(f"{str} have {c} time of {l}")    

n=123456
c=0
con=str(n)
for i in con:
    if int(i)==5:
        c+=1
print(c)
   
#count of occurence of digits which can divisible by 2
n=123456
c=0
con=str(n)
for i in con:
    if int(i)%2==0:
        c+=1
print(c)         

n=123456
c,d=0,4
while n>0: #last digit
    ld=n%10 #ckeck ld and digit
    if ld==d: #count increase when match digit
        c+=1
        n=n//10
print(c)        

n=123456
c=0
d=4
while n>0: 
    ld=n%10 
    if ld%2==0: 
        c+=1
        n=n//10
print(c)   

skills = [
    "python-eAsy",
    "java-difficult",
    "js-easy",
    "react-Easy",
    "html-EASY",
    "git-moderate"
]
for skill in skills:
    if "easy" in skill.lower():
        print(skill) '''

skills = [
    "python-eAsy    ",
    "java-difficult",
    "   easY-js",
    "react-Easy     ",
    "   EASY-html",
    "git-moderate"
]
for skill in skills:
    if "easy" in skill.lower():
        print(skill)            