import math
import time

def fun(num, a):
    time.sleep(a/1000)
    result = math.sqrt(num)
    return result
b = int(input())
c = int(input())
result = fun(b, c)
print(f"sqrt of {b} after {c} milisec is {result}")