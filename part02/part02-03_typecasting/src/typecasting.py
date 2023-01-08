# Write your solution here
number = float(input("Please type in a number:"))
number_int = int(number)
print(f"Integer part: {number_int}")
print(f"Decimal part: {float(number - number_int)}")