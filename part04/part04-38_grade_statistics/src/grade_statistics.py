# Write your solution here

def ask_input():
    list_new = []
    while True:
        grade_input = input("Exam points and exercises completed: ")
        if grade_input == " ":
            break
        elif len(grade_input) == 0:
            break
        else:
            grade_input = grade_input.split()
            exam_1 = int(grade_input[0])
            exe_1 = int(grade_input[1])
        list_new.append(exam_1)
        list_new.append((exe_1 // 10))
    return list_new

def points_inputs(grade):
    points_inputs = (f"Points average: {(sum(grade) / (len(grade)// 2)):.1f}")
    return points_inputs

def pass_percentage(grade):
    passed = 0
    failed = 0
    for i in range(1, len(grade), 2):
        if grade[i-1] < 10:
            failed += 1
        elif (grade[i-1] + grade[i]) < 15:
            failed += 1
        else:
            passed += 1
    pass_inputs = (f"Pass percentage: {((passed / (passed + failed)) * 100):.1f}")
    return pass_inputs

def grade_distriution(grade):
    grade_0 = 0
    grade_1 = 0
    grade_2 = 0
    grade_3 = 0
    grade_4 = 0
    grade_5 = 0
    for i in range(1, len(grade), 2):
        if grade[i-1] < 10:
            grade_0 += 1
        elif (grade[i-1] + grade[i]) < 15:
            grade_0 += 1
        elif (grade[i-1] + grade[i]) < 18:
            grade_1 += 1
        elif (grade[i-1] + grade[i]) < 21:
            grade_2 += 1
        elif (grade[i-1] + grade[i]) < 24:
            grade_3 += 1
        elif (grade[i-1] + grade[i]) < 28:
            grade_4 += 1
        elif (grade[i-1] + grade[i]) < 31:
            grade_5 += 1
    print("Grade distribution:")
    print("  5: "+("*" * grade_5))
    print("  4: "+("*" * grade_4))
    print("  3: "+("*" * grade_3))
    print("  2: "+("*" * grade_2))
    print("  1: "+("*" * grade_1))
    print("  0: "+("*" * grade_0))
               
    
grade = ask_input()

points_average = points_inputs(grade)

pass_print = pass_percentage(grade)



print("Statistics: ")
print(points_average)
print(pass_print)
grade_distriution(grade)
     