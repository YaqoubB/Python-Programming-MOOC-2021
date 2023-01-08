# tee ratkaisusi tänne

class Course:
    def __init__(self, name: str, grade: int, credits: int):   #sample output implies no missing attributes
        self.__name = name
        self.__grade = grade
        self.__credits = credits


    def name(self):
        return self.__name
    
    def grade(self):
        return self.__grade
    
    def credits(self):
        return self.__credits

    def change_grade(self, grade: int):
        if self.__grade < grade:
            self.__grade = grade
    
    def __str__(self):
        return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"


class CourseBook:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if name not in self.__courses:
            self.__courses[name] = Course(name, grade, credits)
        else: 
            self.__courses[name].change_grade(grade)
    
    def get_course(self, name: str):
        if not name in self.__courses:
            return None
        return self.__courses[name]
    
    def amount_courses(self):
        return len(self.__courses)

    def total_credits(self):
        total = 0
        for key in self.__courses:
            total += int(self.__courses[key].credits())
        return total

    def mean_grades(self):
        if len(self.__courses) == 0:
            return 0
        else:
            total = 0
            for key in self.__courses:
                total += int(self.__courses[key].grade())
            return total / len(self.__courses)
    
    def grade_list(self):
        grade_dict = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
        for key, value in self.__courses.items():
            if int(value.grade()) == 5:
                grade_dict[5] += 1
            if int(value.grade()) == 4:
                grade_dict[4] += 1
            if int(value.grade()) == 3:
                grade_dict[3] += 1
            if int(value.grade()) == 2:
                grade_dict[2] += 1
            if int(value.grade()) == 1:
                grade_dict[1] += 1
        return grade_dict
    
    def print_course(self):
        print(self)
        print(f"mean {self.mean_grades():.1f}")
        print("grade distribution")
        grade_list = self.grade_list()
        print("5: "+("x" * grade_list[5]))
        print("4: "+("x" * grade_list[4]))
        print("3: "+("x" * grade_list[3]))
        print("2: "+("x" * grade_list[2]))
        print("1: "+("x" * grade_list[1]))


    def __str__(self):
        return f"{self.amount_courses()} completed courses, a total of {self.total_credits()} credits)"

class CourseBookApplication:
    def __init__(self):
        self.__coursebook = CourseBook()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        name = input("course: ")
        grade = input("grade: ")
        credits = input("credits: ")
        self.__coursebook.add_course(name, grade, credits)

    def get_course_data(self):
        name = input("course: ")
        course = self.__coursebook.get_course(name)
        if course == None:
            print("no entry for this course")
        else:
            print(course)

    def total_courses(self):
        self.__coursebook.print_course()

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.total_courses()   
            else:
                self.help()

application = CourseBookApplication()
application.execute()

    

    