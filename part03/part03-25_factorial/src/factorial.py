# Write your solution here

multiplier = 1
factorial = 1

while True:
    number = int(input("Please type in a number: "))
    multiplier = number
    while number > 0:
        factorial = factorial * (number)
        number -= 1
        if number <= 0:
            print(f"The factorial of the number {multiplier} is {factorial}")
            factorial = 1
            break
        
    else:
        break

print("Thanks and bye!")
    
