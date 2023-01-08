# write your solution here

dictionary_1 = {}
dictionary_2 = {}


student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")



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
                sum = 0

for key, value in dictionary_1.items():
    if key in dictionary_2:
        print(f"{dictionary_1[key]} {dictionary_2[key]}")


