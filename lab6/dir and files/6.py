import os

def create():
    for i in range(65, 91):  # ASCII codes from A to Z
        with open(f"{chr(i)}.txt", 'w') as file:
            file.write(chr(i))