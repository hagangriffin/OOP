

print("Welcome to grade calculator!")
name = input("\nWhat is your name? ")
num_of_courses = input("How many courses do you have? ")
count = num_of_courses
grades_points = 0
grade_list = []
grade_aver
while count != 0:
    grades_points += int(input("What is your grade? "))
    grade_list.append(int(grades_points))

print("\nYour grade average is: ", )
print("\nYour total points are: ", grades_points)
