# Write your solution here
number = int(input("Please type in a number: "))
counter = -1
counter_1 = 0

while counter_1 <= number:
    counter_1 += 2
    counter += 2
    if counter_1 <= number:
        print(counter_1)
    if counter <= number:
        print(counter)