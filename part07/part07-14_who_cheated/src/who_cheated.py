# Write your solution here

import csv

def cheaters():
    dictionary_1 = {}
    list_1 = []
    with open("start_times.csv") as file:
        for line in csv.reader(file, delimiter=";"):
            line[1] = line[1].split(":")
            dictionary_1[line[0]] = []
            dictionary_1[line[0]].append((int(line[1][0]) * 60) + (int(line[1][1])))  #turning hours to mins and adding total mins and then appending key:value to dictionary
        
    with open("submissions.csv") as file:
        for line in csv.reader(file, delimiter=";"):
            for key in dictionary_1:
                if line[0] == key:
                    line[3] = line[3].split(":")
                    dictionary_1[key].append((int(line[3][0]) * 60) + (int(line[3][1])))
    for key, value in dictionary_1.items():
        for i in range(len(value)):
            if value[i] - value[0]  > 180:
                list_1.append(key)
                break
    #print(list_1)
    #print(dictionary_1)
    return list_1


if __name__ == "__main__":
    cheaters()