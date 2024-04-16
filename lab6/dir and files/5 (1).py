import os

pathie = "C:/Users/ASUS/Desktop/pp"

def fun(list_items, pathie):
    with open(pathie, 'w') as file:
        for item in list_items:
            file.write(f"{item}\n")
