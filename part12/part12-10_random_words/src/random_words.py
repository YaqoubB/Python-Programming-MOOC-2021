# Write your solution here:

import random

def word_generator(characters: str, length: int, amount: int):
    for i in range(amount):
        yield ( characters[i:] for i in range(random.randint(0, len(characters) - length)))



if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)