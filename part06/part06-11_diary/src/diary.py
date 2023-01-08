# Write your solution here




print("1 - add an entry, 2 - read entries, 0 - quit")
while True:
    function = int(input("Function: "))
    if function == 1:
        diary_entry = input("Diary entry: ")
        print("Diary saved")
        with open("diary.txt", "a") as file:
            file.write(f"{diary_entry}\n")  
        with open("diary.txt") as file:
            contents = file.read()       
    if function == 2:
        print("Entries:")
        print(contents)
    if function == 0:
        print("Bye now!")
        break





    



