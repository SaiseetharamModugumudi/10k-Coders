s = "hello world"
vowels = "aeiouAEIOU"
count = sum(1 for ch in s if ch in vowels)
print("Vowels:", count)

s = "hello world"
vowels = "aeiouAEIOU"
count = sum(1 for ch in s if ch not in vowels)
print("consonents:", count)

s = "HeLLo"
upper = sum(1 for c in s if c.isupper())
lower = sum(1 for c in s if c.islower())
print("Upper:", upper, "Lower:", lower)

s = "python"
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed:", rev)

s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

n = -5
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

n = 11
print("Even" if n % 2 == 0 else "Odd")

a, b, c = 10, 25, 15
print("Largest of 2:", max(a, b))
print("Largest of 3:", max(a, b, c))

year = 2024
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")

s = "programming"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

s = "programming"
result = ""
for ch in s:
    if ch not in result:
        result += ch
print(result)

sentence = "Python is a powerful programming language"
words = sentence.split()
longest = max(words, key=len)
print("Longest word:", longest)

s = "python is easy and python is powerful"
words = s.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)

s = "python is fun"
print(s.replace(" ", "-"))

s = "PythonDeveloper"
result = ""
for ch in s:
    if ch.isupper() and result:
        result += "_"
    result += ch
print("_" + result + "_")

s = "hello world"
vowels = "aeiouAEIOU"
result = ""
for ch in s:
    if ch in vowels:
        result += "*"
    else:
        result += ch
print(result)

s1, s2 = "listen", "silent"
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

s = "hello world python"
words = s.split()
rev_words = [w[::-1] for w in words]
print(" ".join(rev_words))

s = "abc123xyz45"
digits = "".join([ch for ch in s if ch.isdigit()])
print(digits)

s = "  Python   is   fun  "
print(s.replace(" ", ""))

s = "python"
print("".join(sorted(s)))

age = 20
print("Eligible" if age >= 18 else "Not Eligible")

marks = 82
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

ch = 'e'
if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")

n = 15
if n % 3 == 0 and n % 5 == 0:
    print("Multiple of 3 and 5")
else:
    print("Not Multiple of 3 and 5")

ch = '@'
if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Symbol")

n = 28
print("Divisible by 7" if n % 7 == 0 else "Not Divisible by 7")

age = 65
print("Senior Citizen" if age >= 60 else "Not Senior Citizen")

n = 12
print("Even" if n % 2 == 0 else "Odd")

a, b = 15, 20
print("Largest:", a if a > b else b)

a, b, c = 12, 45, 33
print("Largest:", max(a, b, c))

