# Write your solution here

def formatted(list : float) -> float:
    list_1 = []
    element = 0
    for i in list:
        element = f"{i:.2f}"
        list_1.append(element)
    return list_1
    




if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)