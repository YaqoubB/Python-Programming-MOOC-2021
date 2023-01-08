from math import sqrt
# Write your solution here

while True:
    int_number = int(input("Please type in a number: "))
    if int_number < 0:
        print("Invalid number")
    elif int_number > 0:
        print(sqrt(int_number))
    elif int_number == 0:
        print("Exiting...")
        break
        
