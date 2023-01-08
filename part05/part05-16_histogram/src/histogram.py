def histogram(word :str) -> str:
    list_1 = []
    dictionary_1 = {}
    for i in range(len(word)):
        letter = word[i]
        list_1.append(letter)
    for i in list_1:
        if i not in dictionary_1:
            dictionary_1[i] = 0
        dictionary_1[i] += 1
    for key, value in dictionary_1.items():
        print(key, "*" * value)

if __name__ == "__main__":
    words = "abba"
    histogram(words)