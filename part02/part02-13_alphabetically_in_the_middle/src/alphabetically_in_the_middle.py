# Write your solution here
letter_1 = str(input("1st letter: "))
letter_2 = str(input("2nd letter: "))
letter_3 = str(input("3rd letter: "))

if letter_1 < letter_2 < letter_3 or letter_3 < letter_2 < letter_1:
    print(f"The letter in the middle is {letter_2}")
elif letter_1 < letter_3 < letter_2 or letter_2 < letter_3 < letter_1:
    print(f"The letter in the middle is {letter_3}")
elif letter_2 < letter_1 < letter_3 or letter_3 < letter_1 < letter_2:
    print(f"The letter in the middle is {letter_1}")