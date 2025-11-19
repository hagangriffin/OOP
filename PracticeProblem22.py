class Person:
    def __init__(self, x, y, z):
        self.dob = x
        self.name = y
        self.gender = z

    def dis(self):
        print("Person Name: " + self.name)
        print("Person DOB: " + self.dob)
        print("Person Gender: " + self.gender)
        return ""

class Student(Person):
    def __init__(self, x, y, z, a, b):
        Person.__init__(self, x, y, z)
        self.dept = a
        self.id = b

    def display(self):
        print(Person.dis(self))
        print("Stu Dept: " + self.dept)
        print("Stu ID: " + self.id)

class Faculty(Person):
    def __init__(self, x, y, z, a, b):
        Person.__init__(self, x, y, z)
        self.dept = a
        self.id = b

    def disp(self, value = "", onemore = ""):
        print(Person.dis(self))
        print("Faculty Dept: " + self.dept)
        print("Faculty ID: " + self.id)
        if value != "":
            print("Within Poly", value)


s1 = Student("1/24/1903", "Hagan", "Male", "Engineering", "1")
f1 = Faculty("2/2/2004", "John", "Male", "Coding", "2")
s1.display()
f1.disp("John", "99")