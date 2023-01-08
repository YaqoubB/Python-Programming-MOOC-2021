# Write your solution here

word = str(input("Please type in a string: "))
counter = 0

while counter <= len(word):
    print(word[0:counter])
    counter += 1