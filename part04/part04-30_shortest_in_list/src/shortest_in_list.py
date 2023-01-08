# Write your solution here

def shortest(list : str) -> str:
    short = len(list[0])
    word = ""
    for i in list:
        if len(i) <= short:
            short = len(i)
            word = i
    return word


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)