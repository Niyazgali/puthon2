from functools import reduce

def fun(a, b):
    return a*b

myList=input()
num = [int(x) for x in myList.split()]
result = reduce(fun, num)
print(result)