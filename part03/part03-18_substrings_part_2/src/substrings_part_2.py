# Write your solution here

word = str(input("Please type in a string: "))
counter = -1
word_1 = word[-1]

while counter >= -len(word):
    print(word_1)
    counter -= 1
    if counter < -len(word):
        break
    word_1 = word[counter] + word_1
