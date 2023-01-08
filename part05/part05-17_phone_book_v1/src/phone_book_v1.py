my_dictionary = {"mary": "no number", }

while True:
    request = int(input("command (1 search, 2 add, 3 quit):"))
    if request == 1:
        name = input("name:")
        if name not in my_dictionary:
            my_dictionary[name] = "no number"
        print(f"{my_dictionary[name]}")
    if request == 2:
        name = input("name:")
        number = input("number:")
        print("ok!")
        if name not in my_dictionary:
            my_dictionary[name] = number
        my_dictionary[name] = number
    if request == 3:
        print("quitting...")
        break