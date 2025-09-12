number_1 = int(input("What is the first number? "))
number_2 = int(input("What is the second number? "))
operator = input("Would you like to add, subtract, multiply, or divide? Use symbols for operators.\n")

if operator == "+":
    print(number_1 + number_2)

elif operator == "-":
    print(number_1 - number_2)

elif operator == "*":
    print(number_1 * number_2)

elif operator == "/":
    print(number_1 / number_2)

else:
    print("Invalid operator")