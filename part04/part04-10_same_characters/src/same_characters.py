# Write your solution here

def same_chars(sentence, index_1, index_2):
    if index_1 >= len(sentence) or index_2 >= len(sentence):
        return False
    index_1 = sentence[index_1]
    index_2 = sentence[index_2]
    if index_1 == index_2:
        return True
    else:
        return False



# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 5, 5))