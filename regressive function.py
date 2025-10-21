def myfunc(a):
    if a==1:
        return 1
    return a* myfunc(a-1)
print(myfunc(5))    