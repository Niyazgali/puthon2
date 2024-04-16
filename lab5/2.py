#Write a Python program that matches a string that has an 'a' followed by two to three 'b'

import re

with open(r'C:\Users\User\OneDrive\Рабочий стол\vscode\lab5', 'r', encoding='utf-8') as file:
     g = file.read()

match = re.findall(r"a(bb|bbb)", g)
print(match)