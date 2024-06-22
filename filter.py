def even_numbers(numbers):
    result = []
    for number in numbers:
        if number%2==0:
            result.append(number)
    return result

# print(even_numbers([1,2,3,4,5,6]))
# print(even_numbers(range(10,100)))

def digit_strings(strngs):
    result = []
    for item in strngs:
        if item.isdigit():
            result.append(item)
    return result

# print(digit_strings(["duke","sam","123","33","2swe"]))

people = [
    {"name":"harry","age":23,"gender":"male"},
    {"name":"hermoine","age":24,"gender":"female"},
    {"name":"ron","age":25,"gender":"male"},
]

def male_list(list_dicts):
    result = []
    for item in list_dicts:
        if item["gender"] == "male":
            result.append(item)
    return result

# print(male_list(people))

def filter(list,fn):
    result = []
    for item in list:
        if fn(item):
            result.append(item)
    return result

def even_num(x):
    return x%2 == 0

# print(filter([1,2,3,4,5,6,7,8,9,10],even_num))

def digit_strng(x):
    return x.isdigit()

# print(filter(["duke","sam","123","33","2swe"],digit_strng))

def is_male(x):
    return x["gender"] == "male"

# print(filter(people,males))

""" Notes

Output list will always be equal to or less than in length compared to input list

the custom code (fn) always has to return a bool-- this type of a function is called a predicate

data type of input list items is the same as the output list items


"""
