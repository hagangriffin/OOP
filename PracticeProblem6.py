range_start = int(input("From what number: "))
range_end = int(input("To what number: "))

for e in range(range_start, range_end + 1):
    if e%2 == 0:
        print(str(e) + " Is Even")
    else:
        print(str(e) + " Is Odd")