# write your solution here

import difflib 


check = input("Write text: ")
#check = "this is acually a good and usefull program"

check_split = check.split(" ")
contents = []
mistakes = ""
suggestions = []

with open("wordlist.txt") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        contents.append(line)
    for i in check_split:
        m = i.lower()
        n = f" *{i[:]}*"
        if m not in contents:
            mistakes = mistakes + n
            suggestions.append(i)
        else:
            mistakes = mistakes + " " + i    
   
print(mistakes)
print("suggestions: ")
for i in suggestions:
    store = difflib.get_close_matches(i, contents)
    store = ", ".join(store)
    print(f"{i}: {store}")



