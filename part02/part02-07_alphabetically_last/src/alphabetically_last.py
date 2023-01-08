
word_1 = str(input("Please type in the 1st word: "))
word_2 = str(input("Please type in the 2nd word: "))

if word_1 < word_2:
    print(f"{word_2} comes alphabetically last.")
elif word_1 > word_2:
    print(f"{word_1} comes alphabetically last.")
elif word_1 == word_2:
    print("You gave the same word twice.")
