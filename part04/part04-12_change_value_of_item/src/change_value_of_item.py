# Write your solution here

list = [1, 2, 3, 4, 5]

index = 0

while index != -1:
    index = int(input("Index: "))
    if index == -1:
        continue
    value = int(input("New value: "))
    if index != -1:
        list[index] = value
        print(list)