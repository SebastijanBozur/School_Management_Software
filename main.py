commands = [
    'create',
    'manage',
    'student',
    'teacher',
    'homeroom teacher',
    'class',
    'end',
]


class Student:
    def __init__(self, classes):

        self.first_name = input("Enter student first name/surname name: ")
        self.last_name = input("Enter student last name/family name: ")
        symbol = input("Enter student class: ")
        print()
        self.group = get_group(classes, symbol)
        self.group.students.append(self)
        print(f"First name: {self.first_name.capitalize()}, Last name: {self.last_name.capitalize()}, Class: {self.school_class.upper()}.")

    def print(self):
        for teacher in self.group.teachers:
            print(teacher.subject," - ", teacher.first_name, teacher.last_name)


class Teacher:
    def __init__(self, classes):

        self.first_name = input("Enter teacher first name/surname name: ")
        self.last_name = input("Enter teacher last name/family name: ")
        self.subject = input("Enter teacher subject: ")
        self.groups = []
        print()
        while True:
            symbol = input("Enter the classes they teach: ").upper()
            group = get_group(classes, symbol)
            group.teachers.append(self)
            self.groups.append(group)
            if symbol == "":
                print(f"First name: {self.first_name.capitalize()}, Last name: {self.last_name.capitalize()}, Subject: {self.subject.capitalize()}.")
                print(f"Classes: {self.classes}")
                break

    def print(self):
        for classname in self.classes:
            print(classname)


class Group:
    def __init__(self, symbol):
        self.symbol = symbol
        self.homeroom_teacher = None
        self.students = []
        self.teachers = []

    def print(self):
        if self.homeroom_teacher:
            print(f"Homeroom teacher: {self.homeroom_teacher.first_name}, {self.homeroom_teacher.last_name}")

        else:
            print("Homeroom Teacher not found")

        for student in self.students:
            print(student.first_name, student.last_name)


def get_group(classes, symbol):
    if symbol not in classes:
        classes[symbol] = Group(symbol)
    return classes[symbol]



class Homeroomteacher:
    def __init__(self, classes):

        self.first_name = input("Enter Homeroom Teacher name/surname name: ")
        self.last_name = input("Enter Homeroom Teacher last name/family name: ")
        symbol = input("Enter Homeroom Teacher class: ")
        self.group = get_group(classes, symbol)
        self.group.homeroom_teacher = self
        print()
        print(
            f"First name: {self.first_name.capitalize()}, Last name: {self.last_name.capitalize()}, Class: {self.school_class.upper()}.")

    def print(self):
        for student in self.group.students:
            print(student.first_name, " ", student.last_name)


def menu():
    students = {}
    teachers = {}
    classes = {}
    homeroom_teachers = {}

    while True:
        print()
        print("'create' - to create a user")
        print("'manage' - to manage classes, student and teachers")
        print("'end' - to end program")
        choice = input("Enter your action: ").lower()
        if choice in commands:
            if choice == "create":
                create_user(students, teachers, homeroom_teachers, classes)

            if choice == "manage":
                manage(students, teachers, homeroom_teachers, classes)


            if choice == "end":
                break
        else:
            print()
            print("invalid input!")
            print()


def create_user(students, teachers, homeroom_teachers, classes):
    while True:
        print()
        print("'student' - to create a student")
        print("'teacher' - to create a teacher")
        print("'homeroom teacher' - to create a homeroom teacher")
        print("'end' - to get to first menu")
        option = input("Enter your action: ").lower()
        if option in commands:
            if option == "student":
                user = Student(classes)
                students[user.first_name, user.last_name] = user

            if option == "teacher":
                user = Teacher(classes)
                teachers[user.first_name, user.last_name] = user

            if option == 'homeroom teacher':
                user = Homeroomteacher(classes)
                homeroom_teachers[user.first_name, user.last_name] = user

            if option == "end":
                break
        else:
            print()
            print("invalid input!")
            print()


def manage(students, teachers, homeroom_teachers, classes):
    while True:
        print()
        print("'student' - to manage students")
        print("'teacher' - to manage teachers")
        print("'homeroom teacher' - to manage homeroom teachers")
        print("'end' - to get to first menu")
        option = input("Enter your action: ").lower()
        if option in commands:
            if option == "student":
                first = input("Type student first name: ").capitalize()
                last = input("Type in student last name: ").capitalize()
                if (first, last) in students:
                    students[first, last].print()
                else:
                    print("not present in database")
            if option == "teacher":
                first = input("Type student first name: ").capitalize()
                last = input("Type in student last name: ").capitalize()
                if (first, last) in teachers:
                    students[first, last].print()
                else:
                    print("not present in database")

            if option == 'homeroom teacher':
                first = input("Type student first name: ").capitalize()
                last = input("Type in student last name: ").capitalize()
                if (first, last) in teachers:
                    print()
                else:
                    print("not present in database")

            if option == 'class':
                print()
                symbol = input("Please enter a class: ")
                if symbol in classes:
                    classes[symbol].print()
                print()

            if option == "end":
                break
        else:
            print()
            print("invalid input!")
            print()


menu()