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
        sum = sum + number
    return sum

def product_list(numbers):
    """This function multiplies numbers in a list; if given an empty list it returns none"""
    if len(numbers)==0:
        return None
    product = 1
    for number in numbers:
        product *= number
    return product

def reduce(ls, fn, initial):
    aggregate = initial
    for item in ls:
        aggregate = fn(aggregate, item)
    return aggregate

def plus(a,b):
    return a + b

assert reduce([1,2,3],plus,0) == 6

assert reduce([1,2,3,20,10,99,9],max,-math.inf) == 99

def inc(aggregate, number):
    return aggregate + 1

assert reduce([11,29,300,49,15],inc,0) == 5

def second(aggregate, number):
    return number

assert reduce([1,22,33,55,9],second,None) == 9

def mul(aggregate, number):
    return number * aggregate

assert reduce([1,2,3,5,9],mul,1) == 270

def first(aggregate, number):
    if aggregate == None:
        return number
    else:
        return aggregate

assert reduce([111,22,33,55,9],first,None) == 111

""" Notes

the output will be a single reduced value

the custom code (fn) operates on the current aggregate and the item to produce a new aggregate

the data type of the output would not necessarily be the same as the data type of the input items

"""
