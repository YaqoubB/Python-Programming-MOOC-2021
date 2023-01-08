# Write your solution here

sentence = ""
word_1 = ""
word_2 = ""
while True:
    word_1 = str(input("Please type in a word: "))
    if word_1 == "end":
        break
    if word_1 == word_2:
        break
    sentence += word_1
    word_2 = str(input("Please type in a word: "))
    if word_2 == "end":
        break
    if word_2 == word_1:
        break
    sentence += " " + word_2 + " "
print(f"{sentence}")