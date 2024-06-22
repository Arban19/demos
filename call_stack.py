def append(number):
    last_digit_int = int(number[-1])
    if last_digit_int in range(0,9):
        appended_number = str(number) + str(increment(last_digit_int))
        return appended_number
    elif last_digit_int == 9:
        appended_number = str(number) + "0"
        return appended_number

def increment(number):
    return number + 1

assert append("6") == "67"
assert append("12") == "123"
assert append("713") == "7134"
assert append("9") == "90"
