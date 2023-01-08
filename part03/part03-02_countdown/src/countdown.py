# Fix the program

counter = 0
countdown = True

print("Are you ready?")
number = int(input("Please type in a number: "))

while number > 0 and countdown:
    print(number)
    number -= 1
    counter += 1
    if countdown == 0:
        countdown = False

print("Now!")




