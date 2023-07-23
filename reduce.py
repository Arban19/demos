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

answer_max_number = max_number([-90,-892,-733,-1001,-2344,-8234,-5764,9133])
print("The biggest number in the given data set is "+ str(answer_max_number) +".")


answer_min_number = min_number([12,24,59,-1,22])
print("The smallest number in the date set is " +str(answer_min_number)+ ".")


def sum_list(numbers):
    """ This function adds the numbers in a list; if given an empty list it returns none"""
    if len(numbers)==0:
        return None
    sum = 0
    for number in numbers:
        sum += number
    return sum

answer = sum_list([2,3,4,5,6])
print(answer)

def product_list(numbers):
    """This function multiplies numbers in a list; if given an empty list it returns none"""
    if len(numbers)==0:
        return None
    product = 1
    for number in numbers:
        product *= number
    return product

answer = product_list([21,5])
print(answer)
