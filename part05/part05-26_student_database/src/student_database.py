# Write your solution here

def add_student(students :dict, name: str) ->dict:
    if name not in students:
        students[name] = []
    return students


def add_course(students :dict, name :str, course :tuple):
    if course[1] == 0:
        return
    if name in students:
        if students[name] == []:
            students[name].append(course)
            return
        for i in students[name]:
            if i[0] == course[0]:
                if i[1] < course[1]:
                    students[name].remove(i)
                    students[name].append(course)
                    return
                elif i[1] > course[1]:
                    return
        students[name].append(course)      
            

def print_student(students :dict, name: str):
    grade_sum = 0
    if name in students:
        print(f"{name}:")
        if students[name] == []:
            print(" no completed courses")
        else:
            print(f" {len(students[name])} completed courses:")
            for i in students[name]: #for tuple in list
                print(f"  {i[0]} {i[1]}") #print 0th and 1st index in tuple
                grade_sum += i[1]
            print(f" average grade {grade_sum / len(students[name]):.1f}")
    else:
        print(f"{name}: no such person in the database")

def summary(students):
    print(f"students {len(students)}")
    most = 0
    most_name = ""
    for i in students:
        if len(students[i]) > most:
            most = len(students[i])
            most_name = i
    print(f"most courses completed {most} {most_name}")
    best = 0
    best_name = ""
    for i in students:
        sum = 0
        for j in students[i]: #j here is the tuple
            sum += j[1]
        average = sum / len(students[i])
        if average > best:
            best = average
            best_name = i
    print(f"best average grade {best:.1f} {best_name}")



if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)