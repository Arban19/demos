def add(a,b):
    print("first arg = ", a)
    print("second arg = ", b)
    return a + b

print(add(2,5))
print(add(a=4,b=9))
print(add(b=19,a=2)) # keyword arg
print(add(19,2)) # positional arg
