# Write your solution here

def no_shouting(list : list) -> list:
    list_1 = []
    for i in list:
        if i.isupper() == False:
            list_1.append(i)
    return list_1


if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)