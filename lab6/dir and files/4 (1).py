import os

pathie = "C:/Users/ASUS/Desktop/pp"

def fun(pathie):
    with open(pathie, 'r') as file:
        print("Number of lines:", len(file.readlines()))