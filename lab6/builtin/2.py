def fun(word):
    up=sum(1 for char in word if char.isupper())
    low=sum(1 for char in word if char.islower())

    print ("upper case sum:", up)
    print ("lower case sum:", low)

word=input()

fun(word)