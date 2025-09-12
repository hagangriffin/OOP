from traceback import print_tb
mylist = [1,2,3,4,5,6]
mylist2 = ["Jack", "Bob", "Zachary", "Claire", "Jimmy", "John"]
print("""1. Add Element
2. Remove Element
3. Replace Element
4. Reverse Elements
5. Print Elements
6. Quit""")

while True:
    user_input = int(input("\nWhat is your choice: "))

    if user_input == 1:
        name = input("\nWhat is the name of the person you would you like to add? ")
        age = int(input("What is the age of the person you would like to add? "))
        place = int(input("What place would you like to add it too? "))
        place_adjusted = place - 1
        mylist.append(age)
        mylist2.append(name)

    elif user_input == 2:
        found = False
        ind = 0
        val = "None"
        if len(mylist) == 0:
            print("\nThe list is already empty")
        else:
            print(f"\nThe names currently in the list are: {mylist2}")
            rem = input("What name would you like to remove? ")
            for e in mylist2:
                ind += 1
                if e == rem:
                    mylist2.remove(rem)
                    val = mylist[ind-1]
                    mylist.pop(val)
                    found = True
                    break
            if not found:
                print("That name is not in the list")

    elif user_input == 3:
        e = input("What is the name to be replaced? ")
        new = input("What is the name of the new person? ")
        new_age = int(input("What is the age of the new person? "))
        ind_1 = 0

        for x in mylist2:
            ind_1 += 1
            if x == e:
                mylist.remove(ind_1)

        mylist2.remove(e)
        mylist2.append(new)
        mylist.append(new_age)

        print("\nElement Replaced")

    elif user_input == 4:
        mylist.reverse()
        mylist2.reverse()
        print("Lists reversed")

    elif user_input == 5:
        print(mylist2)
        print(mylist)

    elif user_input == 6:
        break

    else:
        print("Error try again")

    print("\n-------------------------------------------------------------")

print("\nThank you for using my program")