COURSES = {1: 'Algebra 1', 2: 'Algebra 2', 3: 'Geometry 1', 4: 'Geometry 2', 5: 'PreCalculus', 6: 'Calculus',
           7: 'Coding', 8: 'English', 'E': "EXIT"}
Multiplier = 30

student_name = 'Oktay'
student_surname = 'Koc'


def print_all_courses():
    for key, course in COURSES.items():
        print("{} - {}".format(key, course))


def banner():
    print('*' * Multiplier)


class Course():
    def __init__(self, course_name):
        self.course_name = course_name
        self.midterm = 0
        self.final = 0
        self.project = 0
        self.final_score = 0

    def set_grades(self, midterm, final, project):
        self.midterm = midterm
        self.final = final
        self.project = project
        self.calculate_grades()

    def calculate_grades(self):
        self.final_score = self.midterm * 0.3 + self.final * 0.5 + self.project * 0.2

    def course_result(self):
        if 89 < self.final_score:
            letter_grade = "AA"
        elif 69 < self.final_score < 90:
            letter_grade = "BB"
        elif 49 < self.final_score < 70:
            letter_grade = "CC"
        elif 29 < self.final_score < 50:
            letter_grade = "DD"
        elif self.final_score < 30:
            letter_grade = "FF"

        print("Your course result is {}({})".format(letter_grade, self.final_score))
        if letter_grade == 'FF':
            print("Sorry, you failed")
        else:
            print("Congratulations, you passed the {} course".format(self.course_name))

    def __retr__(self):
        pass

    def __str__(self):
        result = "\nCourse Name: {}\nYour grades\n{}\nMidterm: {}\nFinal: {}\nProject: {}\n{}\nYour Final Score: {}\n".format(
            self.course_name, "*" * Multiplier, self.midterm, self.final, self.project, "-" * 11, self.final_score)
        return result


class Student():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.lessons = set()
        self.list_of_courses = {}

    def validation(self, student):
        return student.name.lower() != self.name.lower() or student.surname.lower() != self.surname.lower()

    def print_lessons(self):
        for lesson in self.lessons:
            print(lesson)

    def set_courses(self):
        for index, lesson in enumerate(self.lessons, start=1):
            self.list_of_courses[index] = Course(lesson)

    def print_courses(self):
        for key, course in self.list_of_courses.items():
            print('{} - {}'.format(key, course.course_name))

    def enter_grade(self):
        while True:
            banner()
            try:
                self.print_courses()
                print('press "E" for exit')
                course_key = input("Select your course by order key: ").upper()
                if (course_key == "E"):
                    break
                course_key = int(course_key)
                course = self.list_of_courses[course_key]
                print("Enter your grades")

                # Here should be validate the value is between 0 - 100
                midtern = int(input("Midtern: "))
                final = int(input("Final: "))
                project = int(input("Project: "))
                course.set_grades(midtern, final, project)
                banner()
                course.course_result()
            except:
                continue

    def take_courses(self):
        while len(user_student.lessons) < 5:
            print("Select your courses from the bellow list by enter order number")
            print_all_courses()

            try:
                course_key = input("select your courses: ")
                if course_key == 'q':
                    if len(user_student.lessons) < 3:
                        print("{0}\nYou have to select minimum 3 courses\n{0}".format("*" * Multiplier))
                        continue
                    break
                course_key = int(course_key)
                user_student.lessons.add(COURSES[course_key])
                print("\nYour selected courses below\n{}".format('*' * Multiplier))
                user_student.print_lessons()
                print('-' * Multiplier)
            except:
                print("please select by number")

        print("Your selected courses below")
        user_student.print_lessons()

        self.set_courses()


existed_student = Student(student_name, student_surname)
attempts = 3

while attempts > 0:
    attempts -= 1

    name = input("Name: ")
    surname = input("Surname: ")

    user_student = Student(name.strip(), surname.strip())

    # Validation of User
    if (existed_student.validation(user_student)):
        if (attempts == 0):
            print("Your information is invalid, please try again later.")
            break
        else:
            print("Your information is invalid! please try again.")
            continue

    else:  # If user is valid.
        attempts = 0
        print("hello {} {}".format(user_student.name, user_student.surname))

        banner()
        user_student.take_courses()

        banner()
        print('Enter your grades')
        banner()
        user_student.enter_grade()