# name=['sai','seetharam','kumar']
# import pyttsx3
# data=pyttsx3.init()
# data.setProperty('rate',150)
# data.setProperty('voice',data.getProperty('voices')[1].id)
# data.say('hello world')
# data.runAndWait()

# for i in name:
#     data.say(i)
#     data.runAndWait()

# import pyttsx3

# engine = pyttsx3.init()
# voices = engine.getProperty('voices') 
# engine.setProperty('rate', 100)   # Speed percent (can go over 100)
# engine.setProperty('voice', voices[1].id)  # Try voices[1].id if you have more than one
# engine.say("Koothoda")
# engine.runAndWait()

# import pyttsx3

# names = ['sai', 'seetharam', 'kumar', 'ram', 'john']
# attendance = {}

# engine = pyttsx3.init()
# engine.setProperty('rate', 150)
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)  # Use voices[1].id for female voice if available

# for name in names:
#     engine.say(f"Mark attendance for {name}")
#     engine.runAndWait()
#     status = input(f"Enter attendance for {name} (p/a): ").strip().lower()
#     attendance[name] = 'Present' if status == 'p' else 'Absent'

# print("\nAttendance Record:")
# for name, status in attendance.items():
#     print(f"{name}: {status}")

# lonest word finding in a senetence
# n="python is a programming language"
# lw = ''
# for x in n.split():
#     if len(x)>len(lw):
#         lw=x
# print(lw)        

# import math as m
# print(m.sqrt(16))

# # math modules - pi, sqrt, factorial, pow, floor, ceil, comb, perm, sin, cos, tan, exp, log, fabs, 
# print(m.pi) 
# print(m.factorial(5))
# print(m.pow(2,3))
# print(m.floor(4.6))
# print(m.ceil(4.2))
# print(m.comb(5,2))
# print(m.perm(5,2))
# print(m.sin(30))
# print(m.cos(60))
# print(m.tan(45))
# print(m.exp(2))
# print(m.log(10))
# print(m.fabs(-5.5))

import datetime as dt
from datetime import timedelta
import itertools
import string
# t=dt.datetime.now()
# print(dt.date.today())
# print(t.year)
# print(t.month)
# print(t.day)
# print(t.hour)
# print(t.minute)
# print(t.second)

# # now i want know after 10 days of todays date
# future_date = dt.date.today() + timedelta(days=10)
# print(future_date)

# # now past three days back
# past_date = dt.date.today() - timedelta(days=3)
# print(past_date)

# CODE for caluclating vloumes of all shapes 
# n=int(input('Enter 1 for cube, 2 for cuboid, 3 for cylinder, 4 for sphere, 5 for rectangle: '))
# if n==1:
#     a=int(input('Enter side of cube: '))
#     v=a**3
#     print(f'Volume of cube is {v}')
# elif n==2:
#     l=int(input('Enter length of cuboid: '))
#     b=int(input('Enter breadth of cuboid: '))
#     h=int(input('Enter height of cuboid: '))
#     v=l*b*h
#     print(f'Volume of cuboid is {v}')
# elif n==3:
#     r=int(input('Enter radius of cylinder: '))
#     h=int(input('Enter height of cylinder: '))
#     v=3.14*r*r*h
#     print(f'Volume of cylinder is {v}')
# elif n==4:
#     r=int(input('Enter radius of sphere: '))
#     v=(4/3)*3.14*r*r*r
#     print(f'Volume of sphere is {v}')
# elif n==5:
#     l=int(input('Enter length of rectangle: '))
#     b=int(input('Enter breadth of rectangle: '))
#     v=l*b
#     print(f'Volume of rectangle is {v}')    

# n=10
# for i in range(1,n):
#     print(m.factorial(i))

# code for combobations of alphabets len    is 4 digits 
# n=4
# alphabets = string.ascii_lowercase[:n]  # first n alphabets

# # Combinations of length 4
# print("Combinations of length 4:")
# for combo in itertools.combinations(alphabets, 4):
#     print(''.join(combo))

# # Permutations of length 4
# print("\nPermutations of length 4:")        
# for perm in itertools.permutations(alphabets, 4):
#     print(''.join(perm))
