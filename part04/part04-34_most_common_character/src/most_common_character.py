# Write your solution here


def most_common_character(word : str) -> str:
    best = 0
    for i in word:
        if word.count(i) > best:
            best = word.count(i)
            result = i
    return result




if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))
    second_string = "exemplaryelementary"
    print(most_common_character(second_string))