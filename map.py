def lstsq(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

# print(lstsq([1,2,3,4]))


def title(list_of_words):
    result = []
    for word in list_of_words:
        result.append(word.title())
    return result

# print(title(["duke","is","a","good boy"]))

people = [
    {"name":"harry","age":23},
    {"name":"hermoine","age":24},
    {"name":"ron","age":25},
]

def age(details_of_people):
    result = []
    for detail in details_of_people:
        result.append(detail["age"])
    return result

def map(ls, fn):
    result = []
    for ele in ls:
        result.append(fn(ele))
    return result

def sq(n):
    return n*n

# print(map([1,2,3,4],sq))

def ttl(w):
    return w.title()

# print(map(["duke","is","a","good","boy"],ttl))

def years(detail):
    return detail["age"]

# print(map(people,years))
