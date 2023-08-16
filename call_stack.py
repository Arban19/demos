def next_digit(number):
    return append(number)

def increment(number):
    return number + 1

def append(number):
    last_digit_int = int(number[-1])
    if last_digit_int in range(0,9):
        appended_number = str(number) + str(increment(last_digit_int))
        return appended_number
    elif last_digit_int == 9:
        appended_number = str(number) + "0"
        return appended_number

assert next_digit("6") == "67"
assert next_digit("12") == "123"
assert next_digit("713") == "7134"
assert next_digit("9") == "90"
print("All tests passed!")
