# Write your solution here

list_1 = []
counter = 1

while True:
    print(f"The list is now {list_1}")
    choose = input("a(d)d, (r)emove or e(x)it: ")
    if choose == "d":
        list_1.append(counter)
        counter += 1
    elif choose == "r":
        if len(list_1) == 0:
            break
        list_1.pop(-1)
        counter -= 1
    elif choose == "x":
        break

print("Bye!")