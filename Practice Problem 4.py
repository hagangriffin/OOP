number_of_answers = int(input("How many numbers do you want to compare? "))
ask_great_or_less = input("Would you like to find the greatest or least number? ")
number_number = 1
answer_list = []
current_high = 0
current_low = 0


while number_of_answers != 0:
    answer = int(input("What is the value of number " + str(number_number) + ": "))
    answer_list.append(answer)
    number_of_answers -= 1
    number_number += 1

if ask_great_or_less.lower() == "greatest":
    for e in answer_list:
        if e > current_high:
            current_high = e
    print("\nThe greatest number is: " + str(current_high))

elif ask_great_or_less.lower() == "least":
    current_low = answer_list[0]
    for e in answer_list:
        if e < current_low:
            current_low = e
    print("\nThe least number is: " + str(current_low))

else:
    print("\nInvalid answer")
