import math

def max_number(numbers):
    """ this function returns the max number from a list of numbers; if given an empty list it returns none """
    if not numbers:
        return "Enter number."
    largest_number = -math.inf
    for number in numbers:
        largest_number = number if  number>largest_number else largest_number
    return largest_number

def min_number(numbers):
    """ this function returns the min number from a list of numbers; if given an empty list it returns none"""
    if not numbers:
        return None
    min_number = math.inf
    for number in numbers:
        min_number = number if number<min_number else min_number
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
