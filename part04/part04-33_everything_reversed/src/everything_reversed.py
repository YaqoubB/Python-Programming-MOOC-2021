# Write your solution here

def everything_reversed(list : list) -> list:
    list_1 = []
    for i in list:
        list_1.append((i[-1::-1]))
    return list_1[-1::-1]




if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)