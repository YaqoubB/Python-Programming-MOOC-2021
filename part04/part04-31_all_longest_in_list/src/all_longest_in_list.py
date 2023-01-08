# Write your solution here

def all_the_longest(list :list) -> list:
    best = 0
    long_list = []
    for i in list:
        if len(i) > best:
            best = len(i)
    for i in list:
        if len(i) == best:
            long_list.append(i)
    return long_list







if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result)