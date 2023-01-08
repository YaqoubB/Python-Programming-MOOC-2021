# Write your solution here

word = str(input("Please type in a string: "))

len_less = 20 - len(word)

if len(word) < 20:
    print("*" * len_less + word)

elif len(word) >= 20:
    print(word[0:19])

