# Write your solution here

list_1 = []

while True:
    value = int(input("New item: "))
    list_1.append(value)
    if value != 0:
        print(f"The list now: {list_1}")
        print(f"The list in order: {sorted(list_1)}")
    else:
        print("Bye!")
        break