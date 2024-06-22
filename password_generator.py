""" this program generates passwords for whatever length desired """

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

password_length = int(input("Enter the desired length of password: "))
generated_password = generate_password(password_length)

print("Generated password:", generated_password)
