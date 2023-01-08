# Write your solution here

import datetime

def is_it_valid(pic: str):
    if len(pic) != 11:
        return False
    #pic_day = int(pic[:2])
    #pic_month = int(pic[2:4])
    #pic_year = int(pic[4:6])
    #pic_identifier = int(pic[7:10])
    pic_marker = pic[6:7]
    pic_character = pic[10:11]
    special_string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    user_year = 0
    if pic_marker == "+":
        user_year = "18" + pic[4:6]
    elif pic_marker == "-":
        user_year = "19" + pic[4:6]
    elif pic_marker == "A":
        user_year = "20" + pic[4:6]
    else:
        return False
    try:
        pic_birthdate = datetime.datetime(int(user_year), int(pic[2:4]), int(pic[:2]))
    except ValueError: 
        return False
    age = datetime.datetime.now() - pic_birthdate
    if age.days < 0:
        return False
    special_number = int(pic[:6] + pic[7:10])
    index = special_number % 31
    if pic_character != special_string[index]:
        return False
    return True






