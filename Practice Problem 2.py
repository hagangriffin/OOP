name = input("What is your name? ")
wages = int(input("What are your hourly wages? "))
hours = int(input("How many hours did you work per day? "))
days = int(input("How many days did you work? "))
monthly_wages = wages*hours*days
print(str(monthly_wages))