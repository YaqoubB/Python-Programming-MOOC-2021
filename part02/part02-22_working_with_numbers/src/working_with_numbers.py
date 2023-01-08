# Write your solution here
quantity = 0
sum = 0
positive = 0
negative = 0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    number = int(input("Number: "))
    if number == 0:
        break
    quantity += 1
    if number > 0:
        positive += 1
    if number < 0:
        negative += 1
    sum += number
print("... the program asks for numbers")
print(f"Numbers typed in {quantity}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum / quantity}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")