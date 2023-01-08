# Write your solution here

import random


def words(n: int, beginning: str):
    content = []
    startswith_list = []
    word_list = []
    with open("words.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            content.append(line)
    for i in content:
        if i.startswith(beginning):
            startswith_list.append(i)
    random.shuffle(startswith_list)
    try:
        for i in range(n):
            word_list.append(startswith_list[i])
        return word_list
    except:
        raise ValueError
        raise IndexError



    
if __name__ == "__main__":
    print(words(7, 'of'))
        