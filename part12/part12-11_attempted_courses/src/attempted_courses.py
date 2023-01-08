class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# Write your solution here


def names_of_students(attempts: list):
    return map(lambda x : x.student_name, attempts)

def course_names(attempts: list):
    return map(lambda x : x,set([course.course_name for course in attempts]))



if __name__ == "__main__":
    attempt = CourseAttempt("Peter Python", "Introduction to Programming", 5)
    print(attempt.student_name)
    print(attempt.course_name)
    print(attempt.grade)
    print(attempt)
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Programming", 2)
    course_names([s1, s2, s3])