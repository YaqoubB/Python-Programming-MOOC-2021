# Write your solution here
word = str(input("Please type in a word: "))
character = str(input("Please type in a character: "))
index = 0

while index >= 0 and len(word) >= 3:
    index = word.find(character)
    if len(word[index:]) < 3:
        break
    print(word[index:index+3])
    index += 1
    word = word[index:]
    index = 0
    if len(word) < 3:
        break