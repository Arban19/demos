x = 0 # global state

def foo():
    global x
    x += 1
    return x

print(foo())
print(foo())
print(foo())
print(foo())
x = 12
print(foo())

# x is called "state"
# function calls are independent of each other
# however, here the diff calls to foo all rely on the state
# hence, these diff calls can influence each other
# state stores a value that outlives all the function calls

# function calls live on until they return at which point they're wiped off
# state lives on throughout the life of the program
# global is one of the ways to achieve state
# other ways include classes, closure

def bar():
    y = 0  # local state
    def baz():
        nonlocal y
        y += 1
        return y
    return baz

z = bar()
print(z())
print(z())
print(z())
print(z())
y = 21
print(z())
# function is called multiple times in the same way but it behaves differently
