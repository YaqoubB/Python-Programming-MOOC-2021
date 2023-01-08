# write your solution here


def largest():
    list_1 = []
    with open("numbers.txt") as new_file:
        for i in new_file:
            list_1.append(i)
    return int(max(list_1))



    





