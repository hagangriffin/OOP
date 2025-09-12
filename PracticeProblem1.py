

print("Welcome to grade calculator!")
name = input("\nWhat is your name? ")
num_of_courses = input("How many courses do you have? ")
count = int(num_of_courses)
grades_points = 0
grade_list = []

while count != 0:
    grades_points += int(input("What is your grade? "))
    grade_list.append(int(grades_points))
    count -= 1

grade_average = grades_points / len(grade_list)

if grade_average >= 90:
    print("You got an A")

elif 80 <= grade_average < 90:
    print("You got a B")

elif 70 <= grade_average < 80:
    print("You got a C")

elif 60 <= grade_average < 70:
    print("You got a D")

else:
    print("\nYou got an F")

print("\nYour grade average is: ", grade_average)
print("\nYour total points are: ", grades_points)
