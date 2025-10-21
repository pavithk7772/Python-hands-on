lst=[20,30,15,19,6,10,43,45,25,33]
def myfunc(x):
    return x>=18
newfunc=lambda x:x>=18
print(list(filter(myfunc,lst)))
print(list(filter(lambda x:x>=18,lst)))