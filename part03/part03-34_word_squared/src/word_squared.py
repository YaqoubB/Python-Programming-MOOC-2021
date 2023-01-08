# Write your solution here
def squared(word, length):
    counter = 0
    word = word * (length * length)
    while counter < length:
        print(f"{word[0:length]}")
        word = word[length:]
        counter += 1


# Testing the function
if __name__ == "__main__":
    squared("python", 15)