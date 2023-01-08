# Write your solution here

import string

def change_case(orig_string: str):
    list_1 = list(orig_string)
    for i in range(len(list_1)):
        if list_1[i] .isupper():
            list_1[i] = list_1[i].lower()
        else:
            list_1[i] = list_1[i].upper()
    return "".join(list_1)


def split_in_half(orig_string: str):
    if len(orig_string) % 2 == 0:
        return (orig_string[:len(orig_string) // 2] , orig_string[len(orig_string) // 2:])
    else:
        return (orig_string[:(len(orig_string) -1) // 2] , orig_string[(len(orig_string) - 1) // 2:])

def remove_special_characters(orig_string: str):
    list_1 = list(orig_string)
    list_2 = []
    for i in list_1:
        if i in string.ascii_letters or i == " " or i in string.digits:
            list_2.append(i)
    return "".join(list_2)


if __name__ == "__main__":
    print(change_case("Well hello there!"))
    print(split_in_half("Well hello there!"))
    print(remove_special_characters("This is a test, lets see how it goes!!!11!"))
