lst=[20,30,15,19,6,10,43,45,25,33]
import functools

def myfunc(x,y):
    return x+y

print(functools.reduce(myfunc,lst))