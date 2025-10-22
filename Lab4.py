class Customer:
    def __init__(self, cid="", name="", acc_num="", phone="", email="", balance=0.0):
        self.cid = cid
        self.name = name
        self.acc_num = acc_num
        self.phone = phone
        self.email = email
        self.balance = balance
    def add_customer_info(self):
        self.cid = input("What is the customer ID? ")
        self.name = input("What is the customer name? ")
        self.acc_num = input("What is the account number? ")
        self.phone = input("What is the customer phone number? ")
        self.email = input("What is the customer email? ")
        self.balance = float(input("What is the customer balance? "))

    def debit_from(self, amount):
        self.balance -= amount

    def debit_to(self, amount):
        self.balance += amount

    def display_customer_info(self):
        print("CID: ", self.cid, "Name: ", self.name, "Account Number: ", self.acc_num, "Phone: ", self.phone, "Email: ", self.email, "Balance: ", self.balance)

transfer = []

customer1 = Customer("1", "Hagan", "12345", "501234342", "hagan@gmail.com", 1000.55)
customer2 = Customer("2", "John", "67890", "501785389", "john@gmail.com", 900.55)

#customer1.add_customer_info()
#customer2.add_customer_info()

am = float(input("What is the amount you would like to transfer? "))

customer1.debit_from(am)
customer2.debit_to(am)

customer1.display_customer_info()
customer2.display_customer_info()

#transfer funds from customer 1 to customer 2