# Write your solution here
word = str(input("Please type in a string: "))
substring = str(input("Please type in a substring: "))
index = 0

while len(word) >= len(substring):
    if substring in word:
        index = word.find(substring)
        index_a = index + len(substring)
        word = word[index + len(substring):]
        if len(word) >= len(substring):
            if substring in word:
                index = word.find(substring)
                print(f"The second occurrence of the substring is at index {index + index_a}.")
                break
            else:
                print("The substring does not occur twice in the string.")
                break
        else:
            print("The substring does not occur twice in the string.")
            break
    else:
        print("The substring does not occur twice in the string.")
        break
else:
    print("The substring does not occur twice in the string.")