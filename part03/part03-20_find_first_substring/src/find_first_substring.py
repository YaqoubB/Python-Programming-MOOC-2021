# Write your solution here

word = str(input("Please type in a word: "))
character = str(input("Please type in a character: "))
index = 0
index = word.find(character)

if index >= 0:
    word = word[index:]
    index = 0
    if len(word) >= 3:
        print(word[index:index + 3])

