op="Hello {} welcome to {} after {} years".format("sai","Bng",6)
op1="Hello {0} welcome to {2} after {1} years".format("sai","Bng",6)
op2="Hello {name} welcome to {city} after {num} years".format(name="sai",city="Bng",num=6)
print(op)
print(op1)
print(op2)

ip1=[["hi","hello"],["ha","hm"]]
ip2=ip1.copy()
ip2[0][1]="bye"
print(ip1,ip2)
print("/n")

import copy
i1=[["hi","hello"],["ha","hm"]]
i2=copy.deepcopy(i1)
i2[0][1]="by"
print(i1,i2)

name = " ramesh "
print(len(name.strip()))

line = "sun_rise_in_east"
print(line.split("_", 2))

fruits = ["apple", "banana", "grape"]
fruits.reverse()
print(fruits)

import random

def gen_pin():
    return random.randint(1000, 9999)
print(gen_pin())

cities = ["Hyderabad", "Mumbai", "delhi", "Pune", "chennai", "KOLKATA"]

for city in cities:
    if not city.istitle():
        print(city)

nested = [100, 200, [300, 400, [500, "target"]]]
print(nested[2][2][1])

template = "Hello {user}, your booking in {location} is confirmed for {days} days."
print(template.format(user="Ananya", location="Goa", days=3))