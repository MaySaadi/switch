def add(a,b=None):
    if b is not None:
        return a + b
    else:
        def inner(b):
            return a + b
        return inner
    


print(add(2,5))
print(add(2)(5))