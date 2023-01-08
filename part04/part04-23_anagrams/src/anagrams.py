# Write your solution here

def anagrams(str_1, str_2):
    return sorted(str_1) == sorted(str_2)




if __name__ == "__main__":
    word_1 = "tame"
    word_2 = "meta"
    call = anagrams(word_1, word_2)
    print(call)

