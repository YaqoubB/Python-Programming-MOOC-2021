# Write your solution here


def palindromes(word):
    counter = -1
    word_1 = ""
    while counter > - len(word) - 1:
        word_1 += word[counter]
        counter -= 1
    return word == word_1


while True:
    pali = input("Please type in a palindrome: ")
    if palindromes(pali) == True:
        print(f"{pali} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")


# Note, that at this time the main program should not be written inside
