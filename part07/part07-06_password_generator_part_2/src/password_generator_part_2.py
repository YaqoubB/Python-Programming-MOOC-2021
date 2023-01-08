# Write your solution here

import string
import random

def generate_strong_password(length :int, number :str, special :str):
    list_1 = list(string.ascii_lowercase)
    number_list = list(range(0, 10))
    special_list = ["!", "?" , "=" , "+" , "-" , "(" , ")" , "#"]
    password_list = []
    password = ""
    if number:
        password_list.append(str(random.choice(number_list)))
    if special:
        password_list.append(random.choice(special_list))
    for i in range(length - len(password_list)):
        password_list.append(random.choice(list_1))
    random.shuffle(password_list)
    for i in password_list:
        password += i
    return password

    




