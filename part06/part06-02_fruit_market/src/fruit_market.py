# write your solution here

def read_fruits():
    dictionary_1 = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.split(";")
            dictionary_1[line[0]] = float(line[1])
    return dictionary_1
        


