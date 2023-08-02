def factorial(number):
    if number == 0:
        return 1
    elif number < 0:
        return None
    else:
        factr = 1
        for item in range(1,number + 1):
            factr *= item
    return factr

assert factorial(5) == 120
assert factorial(0) == 1
assert factorial(10) == 3628800
assert factorial(1) == 1
assert factorial(-1) == None
