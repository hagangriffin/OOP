my_line = ["a", "b", "c"]

def stack():
    add = input("What is the name of the person to be added to the queue? ")
    my_line.append(add)
def destack():
    my_line.pop()
def print_stack():
    print(my_line)
while True:
    print("\n1. Add to Stack\n2. Remove from Stack\n3. Print Stack\n4. Exit")
    ch = int(input("What is your choice? "))

    if ch == 1:
       stack()
    elif ch == 2:
        destack()
    elif ch == 3:
        print_stack()
    elif ch == 4:
        print("Have a Good Day")
        break
    else:
        print("Invalid Input, Try Again")