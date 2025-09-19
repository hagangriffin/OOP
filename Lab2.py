myEmployees = {}

while True:

    print("""\n1. Add an Employee\n2. Remove an Employee\n3. Modify an Employee\n4. Display all Employees\n5. Exit Program""")
    choice = int(input("\nWhat would you like to do? "))

    if choice == 1:
        eid = int(input("What is the employee ID? "))
        name = input("What is the employees name? ")
        basicpay = int(input("What is the employees pay? "))
        allowance = int(input("What is the employees allowance? "))
        deductions = int(input("What are the employees deductions? "))
        taxes = int(input("What are the employees taxes? "))
        netpay = basicpay + allowance
        grosspay = netpay - (deductions + taxes)

        myEmployees.update({eid: {"Name": name, "Pay": basicpay, "Allowance": allowance, "Deductions": deductions, "Taxes": taxes, "Net Pay": netpay, "Gross Pay": grosspay}})
        print("\nEmployee Added")

    elif choice == 2:
        rem = int(input("What is the ID of the employee to remove? "))
        found = False
        for e in myEmployees:
            if e == rem:
                del myEmployees[rem]
                found = True
                print("\nEmployee Removed")
                break
            else:
                found = False
        if not found:
            print("That name is not in the list of employees")

    elif choice == 3:
        modid = int(input("What is the ID of the employee to be modified? "))
        there = False
        for e in myEmployees:
            if e == modid:
                there = True
                newname = input("What is the name of the employee? ")
                newbasicpay = int(input("What is the employees pay? "))
                newallowance = int(input("What is the employees allowance? "))
                newdeductions = int(input("What are the employees deductions? "))
                newtaxes = int(input("What are the employees taxes? "))
                newnetpay = newbasicpay + newallowance
                newgrosspay = newnetpay - (newdeductions + newtaxes)

                myEmployees.update({modid: {"Name": newname, "Pay": newbasicpay, "Allowance": newallowance, "Deductions": newdeductions, "Taxes": newtaxes, "Net Pay": newnetpay, "Gross Pay": newgrosspay}})
                print("\nEmployee Modified")
            else:
                there = False

        if not there:
            print("\nThat employee is not in the list")

    elif choice == 4:
        for e in myEmployees.items():
                print("-----------------------")
                print(e)
                print("-----------------------")

    elif choice == 5:
        break

print("Thanks for using my program")
