import os

pathie = "C:/Users/ASUS/Desktop/pp2"

dir = [d for d in os.listdir(pathie) if os.path.isdir(os.path.join(pathie, d))]

files = [f for f in os.listdir(pathie) if os.path.isfile(os.path.join(pathie, f))]

all = os.listdir(pathie)

print("directories: ", dir)
print("files:", files)
print("all items:", all)
