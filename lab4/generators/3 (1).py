def fun(n):
    for i in range(n+1):
        if i % 5 != 0 and (i % 3 == 0 or i % 4 == 0):
            yield i

def div(n):
    generator = fun(n)
    for number in generator:
        print(number, end=", ")

n = int(input())
div(n)
