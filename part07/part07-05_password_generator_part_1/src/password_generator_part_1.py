# Write your solution here

import string
import random

def generate_password(length :int):
    list_1 = list(string.ascii_lowercase)
    password_initial = random.sample(list_1, length)
    password_final = ""
    for i in password_initial:
        password_final += i
    return password_final


