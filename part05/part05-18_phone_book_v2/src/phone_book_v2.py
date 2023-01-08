# Write your solution here

my_dictionary = {}

while True:
    request = int(input("command (1 search, 2 add, 3 quit):"))
    if request == 1:
        name = input("name:")
        if name not in my_dictionary:
            print("no number")
        else:
            list_1 = my_dictionary[name]
            for i in range(len(list_1)):
                print(list_1[i])
    if request == 2:
        name = input("name:")
        number = input("number:")
        print("ok!")
        if name not in my_dictionary:
            my_dictionary[name] = []
            my_dictionary[name].append(number)
        else:
            my_dictionary[name].append(number)
    if request == 3:
        print("quitting...")
        break