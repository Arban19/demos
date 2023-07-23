import math

def max_number(numbers):
    """ this function returns the max number from a list of numbers; if given an empty list it returns none """
    if len(numbers)==0:
        return None
    largest_number = -math.inf
    for number in numbers:
        if number>largest_number:
            largest_number = number
    return largest_number

def min_number(numbers):
    """ this function returns the min number from a list of numbers; if given an empty list it returns none"""
    if len(numbers)==0:
        return None
    min_number = math.inf
    for number in numbers:
        if number<min_number:
            min_number=number
    return min_number

def sum_list(numbers):
    """ This function adds the numbers in a list; if given an empty list it returns none"""
    if len(numbers)==0:
        return None
    sum = 0
    for number in numbers:
        sum += number
    return sum

def product_list(numbers):
    """This function multiplies numbers in a list; if given an empty list it returns none"""
    if len(numbers)==0:
        return None
    product = 1
    for number in numbers:
        product *= number
    return product
