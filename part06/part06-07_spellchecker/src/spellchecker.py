# write your solution here

if True:
    check = input("Write text: ")
else:
    check = "usefull"

check_split = check.split(" ")
contents = []
mistakes = ""

with open("wordlist.txt") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        contents.append(line)
    for i in check_split:
        m = i.lower()
        n = f" *{i[:]}*"
        if m not in contents:
            mistakes = mistakes + n
        else:
            mistakes = mistakes + " " + i
        


     
print(mistakes)


