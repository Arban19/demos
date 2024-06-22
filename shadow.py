z = "Duke"

def foo():
    z = 0   # local z is shadowing the global z
    print(z)

print(z)
foo()
print(z)


def bar(x):
    local_print = lambda x: print(x)
    local_print(10)
    print(x)


bar(5)
