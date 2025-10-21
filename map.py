lst=['hi','hello','greens','world']

def myfunc(x):
    return len(x)
ans =list(map(myfunc,lst))
print(ans)