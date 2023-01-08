# Write your solution here

number = 2

while number <= 30:
    print(number)
    number += 1
    if number % 2 != 0:
        number += 1
        continue
    if number == 30:
        break
