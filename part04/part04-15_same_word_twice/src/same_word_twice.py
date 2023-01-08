# Write your solution here

list_1 = []

counter = 0

while True:
    word = input("Word: ")
    if word in list_1:
        print(f"You typed in {counter} different words")
        break
    counter += 1
    list_1.append(word)