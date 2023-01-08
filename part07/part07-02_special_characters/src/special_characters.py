# Write your solution here

import string

def separate_characters(my_string: str):
    lower_upper = ""
    punctuation = ""
    other = ""
    for i in range(len(my_string)):
        if my_string[i] in string.ascii_letters:
            lower_upper += my_string[i]
        elif my_string[i] in string.punctuation:
            punctuation += my_string[i]
        else:
            other += my_string[i]
    return lower_upper , punctuation , other


if __name__ == "__main__":
    print(separate_characters("abc.!åäö"))