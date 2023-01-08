# Write your solution here
integer_1 = int(input("Please type in the first number: "))
integer_2 = int(input("Please type in another number: "))

if integer_1 > integer_2:
    print(f"The greater number was: {integer_1}")
elif integer_1 < integer_2:
    print(f"The greater number was: {integer_2}")
else:
    print("The numbers are equal!")