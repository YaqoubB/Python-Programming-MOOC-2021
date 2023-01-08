# tee ratkaisu tänne

# write your solution here

dictionary_1 = {} # id and name
dictionary_2 = {} # id and no of exercises
dictionary_3 = {} # id and exercise points
dictionary_4 = {} # id and exam points
dictionary_5 = {} # id and total points
dictionary_6 = {} # id and grade



if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
else:
    # now this is the False branch, and is never executed
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"





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
                dictionary_2[line[0]] = sum 
                dictionary_3[line[0]] = (sum * 0.25) // 1
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
                dictionary_4[line[0]] = sum 
                sum = 0

for key, value in dictionary_3.items():
    if key in dictionary_4:
        dictionary_5[key] = dictionary_3[key] + dictionary_4[key]

for key, value in dictionary_5.items():
    if value < 15:
        dictionary_6[key] = 0
    elif value < 18:
        dictionary_6[key] = 1
    elif value < 21:
        dictionary_6[key] = 2
    elif value < 24:
        dictionary_6[key] = 3
    elif value < 28:
        dictionary_6[key] = 4
    elif value >= 28:
        dictionary_6[key] = 5


print("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade")
for key, value in dictionary_1.items():
    if key in dictionary_2:
        if key in dictionary_3:
            if key in dictionary_4:
                if key in dictionary_5:
                    if key in dictionary_6:
                        print(f"{value:30}{dictionary_2[key]:<10}{dictionary_3[key]:<10.0f}{dictionary_4[key]:<10}{dictionary_5[key]:<10.0f}{dictionary_6[key]:<10}")


    