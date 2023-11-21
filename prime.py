def is_prime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    for i in range(3,x):
        if x % i == 0 or x % 2 == 0:
            return False
    return True


assert is_prime(19) == True
assert is_prime(21) == False
assert is_prime(2) == True
assert is_prime(-11) == False
assert is_prime(0) == False
assert is_prime(100) == False
assert is_prime(29) == True
