import os

pathie = "C:/Users/ASUS/Desktop/pp2"

if os.path.exists(pathie):
    print("exists")
else:
    print("does not exist")


if os.access(pathie, os.R_OK):
    print("readable")
else:
    print("not readable")


if os.access(pathie, os.W_OK):
    print("writable")
else:
    print("not writable")


if os.access(pathie, os.X_OK):
    print("executable")
else:
    print("not executable")

