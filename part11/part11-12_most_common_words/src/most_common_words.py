# WRITE YOUR SOLUTION HERE:

import string

def most_common_words(filename: str, lower_limit: int):
    list1 = open(filename).read().replace("\n", "").replace(".", " ").replace(",", " ").split(" ")
    return {word : list1.count(word) for word in list1 if word not in string.punctuation and list1.count(word) >= lower_limit}



if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))
    