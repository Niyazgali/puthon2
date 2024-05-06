import os
c = os.getcwd()
check = os.listdir(c)

print(check)

if "1.py" in check and "phonebook.csv" in check:
    print("yes")
else:
    print("no")