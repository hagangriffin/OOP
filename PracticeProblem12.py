my_line = ["a", "b", "c"]

def queue():
    add = input("What is the name of the person to be added to the queue? ")
    my_line.append(add)
def dequeue():
    my_line.remove(my_line[0])
def print_queue():
    print(my_line)
while True:
    print("\n1. Add to Queue\n2. Remove from Queue\n3. Print Queue\n4. Exit")
    ch = int(input("What is your choice? "))

    if ch == 1:
       queue()
    elif ch == 2:
        dequeue()
    elif ch == 3:
        print_queue()
    elif ch == 4:
        print("Have a Good Day")
        break
    else:
        print("Invalid Input, Try Again")