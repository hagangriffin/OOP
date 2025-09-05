
while True:
    print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Quit")
    operator = input("Enter your Choice: ")
    if operator == "5":
        break
    n1 = int(input("\nWhat is the first number? "))
    n2 = int(input("What is the second number? "))

    addition = n1 + n2
    subtraction = n1 - n2
    multiplication = n1 * n2
    division = n1 / n2

    if operator == "1":
        print(f"\n{n1} plus {n2} equals {addition}")
        print("\n------------------------------------------------")
    elif operator == "2":
        print(f"\n{n1} minus {n2} equals {subtraction}")
        print("\n------------------------------------------------")
    elif operator == "3":
        print(f"\n{n1} times {n2} equals {multiplication}")
        print("\n------------------------------------------------")
    elif operator == "4":
        print(f"\n{n1} divided by {n2} equals {division}")
        print("\n------------------------------------------------")
    else:
        print("\nError try again")

print("\nThanks for using my program")