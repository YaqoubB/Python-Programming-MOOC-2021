# Write your solution here

list_1 = []
counter = 1
number = 1

while number > 0:
    number = int(input("How many items: "))
    while counter <= number:
        value = int(input(f"Item {counter}: "))
        list_1.append(value)
        counter += 1
    break

print(list_1)
        