# Write your solution here

def first_word(sentence):
    if sentence.find(" ") > 0:
        return sentence[0:sentence.find(" ")]
    return sentence

def second_word(sentence):
    if sentence.find(" ") > 0:
        sentence = sentence[sentence.find(" ") + 1:]
        if sentence.find(" ") > 0:
            return sentence[0:sentence.find(" ")]
        return sentence


def last_word(sentence):
    if sentence.find(" ") > 0:
        index = -1
        while sentence[index] != " ":
            index -= 1
        return sentence[index + 1:]

    return sentence



# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))