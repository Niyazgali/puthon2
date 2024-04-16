#Write a Python program to convert a given camel case string to snake case.
import re

def fun(c):
    s = re.sub(r'(?<=[a-zа-я0-9])([A-ZА-Я])', r'_\1', c)
    return s.lower()

with open(r'C:\Users\ASUS\Desktop\pp2\lab5\a.txt', 'r', encoding='utf-8') as file:
    g = file.read()

result = fun(g)
print(result)

