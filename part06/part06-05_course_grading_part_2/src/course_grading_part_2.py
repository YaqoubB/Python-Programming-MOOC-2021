# write your solution here

dictionary_1 = {}
dictionary_2 = {}
dictionary_3 = {}
dictionary_4 = {}
dictionary_5 = {}




student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")




with open(student_info) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        line = line.split(";")
        for word in line:
            if line[0] == "id":
                continue
            else:
                dictionary_1[line[0]] = f"{line[1]} {line[2]}"

with open(exercise_data) as new_file:
    sum = 0
    for line in new_file:
        line = line.replace("\n", "")
        line = line.split(";")
        for word in line:
            if line[0] == "id":
                continue
            else:
                for i in range(1,len(line[:])):
                    add = int(line[i])
                    sum += add
                dictionary_2[line[0]] = sum * 0.25
                sum = 0     

with open(exam_data) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        line = line.split(";")
        for word in line:
            if line[0] == "id":
                continue
            else:
                for i in range(1,len(line[:])):
                    add = int(line[i])
                    sum += add
                dictionary_3[line[0]] = sum 
                sum = 0

for key, value in dictionary_2.items():
    if key in dictionary_3:
        dictionary_4[key] = dictionary_2[key] + dictionary_3[key]

for key, value in dictionary_4.items():
    if value < 15:
        dictionary_5[key] = 0
    elif value < 18:
        dictionary_5[key] = 1
    elif value < 21:
        dictionary_5[key] = 2
    elif value < 24:
        dictionary_5[key] = 3
    elif value < 28:
        dictionary_5[key] = 4
    elif value >= 28:
        dictionary_5[key] = 5



for key, value in dictionary_1.items():
    if key in dictionary_5:
        print(f"{value} {dictionary_5[key]}")