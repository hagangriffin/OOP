from traceback import print_tb

students = {1: {"Name": "Hagan", "Major": "CS", "Year": "Freshman", "Credits": 13, "GPA": 3.5}}
print("""1. Add Element
2. Remove Element
3. Replace Element
4. Print Elements
5. Quit""")

while True:
    user_input = int(input("\nWhat is your choice: "))

    if user_input == 1:

        sid = int(input("What is the new student ID? "))
        name = input("What the new name? ")
        major = input("What the new major? ")
        year = input("What the new year? ")
        total_credits = int(input("How many credits do they have? "))
        gpa = float(input("What is their gpa? "))



    elif user_input == 2:
        found = False
        ind = 0
        val = "None"
        if len(students) == 0:
            print("\nThe list is already empty")
        else:
            print(f"\nThe names currently in the list are: {students}")
            rem = int(input("What ID of the student you would like to remove? "))
            for e in students:
                if e == rem:
                    del students[e]
                    found = True
                    break
            if not found:
                print("That name is not in the list")

    elif user_input == 3:
        e = int(input("What is the ID to be replaced? "))
        sid_rep = int(input("What is the new student ID? "))
        name_rep = input("What the new name? ")
        major_rep = input("What the new major? ")
        year_rep = input("What the new year? ")
        total_credits_rep = int(input("How many credits do they have? "))
        gpa_rep = float(input("What is their gpa? "))

        del students[e]

        students.update({sid_rep: {"Name": name_rep, "Major": major_rep, "Year": year_rep, "Credits": total_credits_rep, "GPA": gpa_rep}})

        print("\nElement Replaced")

    elif user_input == 4:
        if len(students) > 0:
            print("\n")
            for student in students.items():
                for x in student:
                    print(x)
                    print("------------")
        else:
            print("The list is empty")

    elif user_input == 5:
        break

    else:
        print("Error try again")

    print("\n-------------------------------------------------------------")

print("\nThank you for using my program")