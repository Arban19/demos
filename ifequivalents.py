def and_eq(x):
    print(x)
    if type(x) == str:
        print(len(x))
    elif type(x) == int:
        if x%2 == 0:
            print("even")

def and_eq_alt(x):
    print(x)
    if type(x) == str:
        print(len(x))
    elif type(x) == int and x%2 == 0:
        print("even")


def or_eq(x):
    print(x)
    if x > 0:
        print("non-zero")
    elif x < 0:
        print("non-zero")

def or_eq_alt(x):
    print(x)
    if x>0 or x<0:
        print("non-zero")

def return_eq(x):
    if x%2 == 0:
        return True
    return False

def return_eq_alt(x):
    return x%2 == 0
