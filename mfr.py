characters = [
    {"name": "Harry Potter", "house": "Gryffindor", "gender": "Male", "age": 11},
    {"name": "Hermione Granger", "house": "Gryffindor", "gender": "Female", "age": 11},
    {"name": "Ron Weasley", "house": "Gryffindor", "gender": "Male", "age": 11},
    {"name": "Albus Dumbledore", "house": "Gryffindor", "gender": "Male", "age": 115},
    {"name": "Severus Snape", "house": "Slytherin", "gender": "Male", "age": 38},
    {"name": "Minerva McGonagall", "house": "Gryffindor", "gender": "Female", "age": 70},
    {"name": "Sirius Black", "house": "Gryffindor", "gender": "Male", "age": 36},
    {"name": "Remus Lupin", "house": "Gryffindor", "gender": "Male", "age": 34},
    {"name": "Hagrid", "house": "Gryffindor", "gender": "Male", "age": 63},
    {"name": "Ginny Weasley", "house": "Gryffindor", "gender": "Female", "age": 11},
    {"name": "Fred Weasley", "house": "Gryffindor", "gender": "Male", "age": 11},
    {"name": "George Weasley", "house": "Gryffindor", "gender": "Male", "age": 11},
    {"name": "Luna Lovegood", "house": "Ravenclaw", "gender": "Female", "age": 11},
    {"name": "Neville Longbottom", "house": "Gryffindor", "gender": "Male", "age": 11},
    {"name": "Draco Malfoy", "house": "Slytherin", "gender": "Male", "age": 11},
    {"name": "Cho Chang", "house": "Ravenclaw", "gender": "Female", "age": 11},
    {"name": "Cedric Diggory", "house": "Hufflepuff", "gender": "Male", "age": 17},
    {"name": "Bellatrix Lestrange", "house": "Slytherin", "gender": "Female", "age": 47},
    {"name": "Voldemort", "house": "Slytherin", "gender": "Male", "age": 71},
]
def sum_male_age(data):
    sum = 0
    for character in data:
        if character["gender"] == "Male":   #filtering character by gender
            age = character["age"]          #mapping each character to their age
            sum += age                      #reducing the age to sum
    return sum

# print(sum_male_age(characters))

from functools import reduce

def is_male(x):
    return x["gender"] == "Male"

# print(list(filter(is_male,characters)))

def age(item):
    return item["age"]

# print(list(map(age,characters)))

from functools import reduce

def total_age(x,y):
    return x + y

# print(reduce(total_age,map(age,filter(is_male,characters))))

def sum_male_age_mfr(data):
    males = filter(is_male,data)
    age_of_males = map(age,males)
    sum_of_ages = reduce(total_age,age_of_males)
    return sum_of_ages

print(sum_male_age_mfr(characters))
