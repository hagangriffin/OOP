my_students = {}
while True:

    cont = int(input("Would you like to: \n1. Add a student \n2. Search for a student \n3. Exit\n"))

    if cont == 1:


        sid = int(input("What is your student ID? "))
        name = input("What is your name? ")
        major = input("What is your major? ")
        year = input("what is your year? ")
        total_credits = int(input("How many credits do you have? "))
        gpa = float(input("What is your gpa? "))


        my_students.update({sid: {"Name": name, "Major": major, "Year": year, "Credits": total_credits, "GPA": gpa}})

    elif cont == 2:
        st_id = int(input("What is the ID of the student? "))
        for e in my_students.items():
            print(e)
            print("---------------------")

    elif cont == 3:
        break

    else:
        print("Invalid Input, Try Again")