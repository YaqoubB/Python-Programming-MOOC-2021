# Write your solution here


while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = int(input("Function: "))
    if function == 1:
        finnish = input("The word in Finnish: ")
        english = input("The word in English: ")
        print("Dictionary entry added")
        with open("dictionary.txt", "a") as file:
            file.write(f"{english};{finnish}\n")
    if function == 2:
        search = input("Search term: ")
        with open("dictionary.txt") as file:
            for line in file:
                if search in line:
                    line = line.replace("\n","")
                    line = line.split(";")
                    print(f"{line[1]} - {line[0]}")
    if function == 3:
        print("Bye!")
        break

