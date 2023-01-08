# Write your solution here

word = str(input("Please type in a string: "))
length = len(word)
counter = 1

while counter <= length:
    print(word[length - counter])
    counter += 1

