def next_digit(digits):
    return append(digits)

def increment(number):
    return number + 1

def append(number):
    last_digit_int = int(number[-1])
    return str(number) + str(increment(last_digit_int))

assert next_digit("6") == "67"
assert next_digit("12") == "123"
assert next_digit("713") == "7134"
# assert next_digit("9") == "90"
print("All tests passed!")

# subproblems
# - increment a number
# - preserve the entire input string
# - get last digit from the input string
# - concat input string with incremented
