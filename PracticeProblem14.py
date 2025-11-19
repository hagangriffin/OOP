


class Student:
    def __init__(self):
        self.sid = 0
        self.name = ""
        self.dob = ""
        self.major = ""
        self.gpa = 0.0
        self.courses = []
    def add_student(self):
        self.sid = int(input("What is your student ID? "))
        self.name = input("What is your name? ")
        self.dob = input("What is your date of birth? ")
        self.major = input("What is your major? ")
        self.gpa = float(input("What is your gpa? "))

        print("Added")
    def update_student(self):
        while True:
            print("\n1. Update Name\n2. Update DOB\n3. Update Major\n4. Update GPA\n5. Exit Updater")
            inp = int(input("What would you like to update? "))
            if inp == 1:
                self.name = input("What is the new name? ")
            elif inp == 2:
                self.dob = input("What is the new DOB? ")
            elif inp == 3:
                self.major = input("What is the new Major? ")
            elif inp == 4:
                self.gpa = float(input("What is the new GPA? "))
            elif inp == 5:
                break
            else:
                print("Invalid Input")

    def register_courses(self, c1):
        self.courses.append(c1)


    def display_student(self):
        print("\nName: ", self.name, "\nDOB: ", self.dob, "\nMajor: ", self.major, "\nGPA: ", self.gpa)
        for e in self.courses:
            print("Courses: ", e.cname)

class Course:
    def __init__(self):
        self.cid = ""
        self.cname = ""
    def add_course(self):
        self.cid = int(input("What is the CID? "))
        self.cname = input("What is the course name? ")

c1 = Course()
c1.add_course()
s1 = Student()
s1.add_student()
s1.register_courses(c1)

s1.display_student()
