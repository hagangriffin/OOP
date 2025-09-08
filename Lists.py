from traceback import print_tb
mylist = []
print("""1. Add Element
2. Remove Element
3. Pop Last Element
4. Print List
5. Quit""")

while True:
    user_input = int(input("\nWhat is your choice: "))

    if user_input == 1:
        add = int(input("\nWhat would you like to add? "))
        place = int(input("What place would you like to add it too? "))
        add_adjusted = add - 1
        mylist.insert(add_adjusted, place)

    elif user_input == 2:
        if len(mylist) == 0:
            print("\nThe list is already empty")
        else:
            rem = int(input("\nWhat element would you like to remove? "))
            for e in mylist:
                if rem == e:
                    mylist.remove(rem)
                else:
                    print("\nThat number is not in the list")
                    print(f"The numbers currently in the list are {mylist}")

    elif user_input == 3:
        mylist.pop()
        print("\nLast element popped")

    elif user_input == 4:
        print(mylist)

    elif user_input == 5:
        break

    else:
        print("Error try again")

    print("\n-------------------------------------------------------------")

print("\nThank you for using my program")