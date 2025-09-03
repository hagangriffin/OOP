owed = float(input("How much do you owe? "))
time = int(input("How many months will you pay it off in? "))
interest = float(input("What is the interest rate in percent? ")) / 100
monthly_interest = interest / 12
months_remaining = time

while months_remaining > 0:
    monthly_pay = owed / months_remaining
    monthly_pay_interest = monthly_pay + monthly_pay*monthly_interest

    if owed < monthly_pay_interest:
        difference = owed
        owed -= difference
        print(f"\nLast month! Payment is {difference}")
        print(f"New total is {owed}")
        break

    print(f"\nTotal owed is {owed}")
    print(f"Monthly payment is {monthly_pay_interest}")
    owed -= monthly_pay_interest
    print(f"New total is {owed}")
    months_remaining -= 1
