z = "Duke"

def foo():
    z = 0   # local z is shadowing the global z
    print(z)

print(z)
foo()
print(z)
