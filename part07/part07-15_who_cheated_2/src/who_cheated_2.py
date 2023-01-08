# Write your solution here

import csv
import datetime

def final_points():
    start_times = {}
    submissions = {}
    grade_dictionary = {}
    with open("start_times.csv") as file:
        for line in csv.reader(file, delimiter=";"):
            name = line[0]
            time = datetime.datetime.strptime(line[1], "%H:%M")
            start_times[name] = time
    for key, value in start_times.items():        
        with open("submissions.csv") as file:
            for line in csv.reader(file, delimiter=";"):
                if line[0] != key:
                    continue
                else:
                    if datetime.datetime.strptime(line[3], "%H:%M") - value > datetime.timedelta(hours = 3):
                        continue
                    else:
                        if key not in submissions:
                            submissions[key] = {}
                            submissions[key][line[1]] = int(line[2])
                        else:
                            if line[1] not in submissions[key]:
                                submissions[key][line[1]] = int(line[2])
                            else:
                                if submissions[key][line[1]] < int(line[2]):
                                    submissions[key][line[1]] = int(line[2])
        for key, value in submissions.items():
            sum = 0
            for i in value:
                sum += value[i]
            grade_dictionary[key] = sum
            sum = 0
    return grade_dictionary



if __name__ == "__main__":
    final_points()