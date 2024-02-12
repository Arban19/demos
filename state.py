x = 0

def foo():
    global x
    while x < 2:
        x += 1
        return x

print(foo())
print(foo())
print(foo())
print(foo())

# x is called "state"
# function calls are independent of each other
# however, here the diff calls to foo all rely on the state
# hence, these diff calls can influence each other

# function calls live on until they return at which point they're wiped off
# state lives on throughout the life of the program
# global is one of the ways to achieve state
# other ways include classes, closure
