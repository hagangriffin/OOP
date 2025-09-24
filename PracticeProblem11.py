def rec():
    l = int(input("What is the length? "))
    w = int(input("What is the width? "))
    print("\nThe area is: ", l*w)

def vol_cube():
    l = int(input("What is the length? "))
    w = int(input("What is the width? "))
    h = int(input("What is the height? "))
    print("\nThe volume is: ", l*w*h)

def area_cir():
    r = int(input("What is the radius? "))
    print("\nThe area is: ", 3.14*r*r)

def circ_cir():
    r = int(input("What is the radius? "))
    print("\nThe volume is: ", 2*3.14*r)

def vol_sphere():
    r = int(input("What is the radius? "))
    print("\nThe volume is: ", (4/3)*3.14*r*r*r)

while True:
    print("\n1. Area of a Rectangle\n2. Volume of a Cube\n3. Area of a Circle\n4. Volume of a Circle\n5. Volume of a Sphere\n6. Exit")
    inp = int(input("\nWhat is your choice? "))

    if inp == 1:
        rec()
    elif inp == 2:
        vol_cube()
    elif inp == 3:
        area_cir()
    elif inp == 4:
        circ_cir()
    elif inp == 5:
        vol_sphere()
    elif inp == 6:
        print("Have a good day")
        break
    else:
        print("Invalid Input, Try Again")