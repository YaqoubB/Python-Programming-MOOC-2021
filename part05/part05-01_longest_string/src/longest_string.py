# Write your solution here

def longest(string_list: list) -> list:
    long = 0
    long_word = ""
    for i in string_list:
        if len(i) > long:
            long = len(i)
            long_word = i
    return long_word





if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))