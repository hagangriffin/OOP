import pickle

class Customer:
    def __init__(self, cid="", name="", acc_num="", phone="", email="", balance=0.0):
        self.cid = cid
        self.name = name
        self.acc_num = acc_num
        self.phone = phone
        self.email = email
        self.balance = balance
        self.credit_cards = []
        self.debit_cards = []
    def add_customer_info(self):
        self.cid = input("What is the customer ID? ")
        self.name = input("What is the customer name? ")
        self.acc_num = input("What is the account number? ")
        self.phone = input("What is the customer phone number? ")
        self.email = input("What is the customer email? ")
        self.balance = float(input("What is the customer balance? "))
        new_customer = Customer(self.cid, self.name, self.acc_num, self.phone, self.email, self.balance)
        customers.append(new_customer)

    def debit_from(self, amount):
        self.balance -= amount

    def debit_to(self, amount):
        self.balance += amount

    def display_customer_info(self):
        print("CID: ", self.cid, "Name: ", self.name, "Account Number: ", self.acc_num, "Phone: ", self.phone, "Email: ", self.email, "Balance: ", self.balance)

class Card:
    def __init__(self, name="", c_type="", card_nm="", cvv="", expiry="", balance=0.0):
        self.name = name
        self.type = c_type
        self.card_nm = card_nm
        self.cvv = cvv
        self.expiry = expiry
        self.c_balance = balance

    def create_card(self):
        self.name = input("What is the name on the card? ")
        self.type = input("What is the card type? ")
        self.card_nm = input("What is the card number? ")
        self.cvv = input("What is the cvv? ")
        self.expiry = input("What is the expiry date? ")
        self.c_balance = float(input("What is the card balance? "))
        new_card = Card(self.name, self.type, self.card_nm, self.cvv, self.expiry, self.c_balance)
        cards.append(new_card)

    def display_cards(self):
        print("Name: ", self.name, "Type: ", self.type, "Card Number: ", self.card_nm, "CVV: ", self.cvv, "Expiry: ", self.expiry, "Balance: ", self.c_balance)

customer1 = Customer("1", "Hagan", "12345", "501234342", "hagan@gmail.com", 1000.55)
customer2 = Customer("2", "John", "67890", "501785389", "john@gmail.com", 900.55)

card1 = Card("Hagan", "Credit", "1234567890", "123", "12 Sept 2028", 1000.45)
card2 = Card("John", "Debit", "0987654321", "321", "14 June 2031", 1235.12)

customers = [customer1, customer2]
cards = [card1, card2]

while True:
    print("\n1. Create Customer\n2. Create Card\n3. Transfer Funds\n4. Assign Card to Customer\n5. Display Customer Info\n6. Display Card Info\n7. Save Data\n8. Exit")
    ch = int(input("What is your choice? "))

    if ch == 1:
        n_customer = Customer()
        n_customer.add_customer_info()
    elif ch == 2:
       n_card = Card()
       n_card.create_card()
    elif ch == 3:
        from_acc = input("What is the account to transfer from? ")
        am = float(input("What is the amount to be transferred? "))
        to_acc = input("What is the account to transfer to? ")

        for a in customers:
            if a.name.lower() == from_acc.lower():
                a.balance -= am
                for n in customers:
                    if n.name.lower() == to_acc.lower():
                        n.balance += am
        print("Money Transferred")
    elif ch == 4:
        cd = input("What is the name on the card? ")
        ac = input("What is the name on the account to add the card to? ")
        for j in cards:
            if j.name.lower() == cd.lower():
                for k in customers:
                    if k.name.lower() == ac.lower():
                        if j.type.lower() == "credit":
                            k.credit_cards.append(j)
                            cards.remove(j)
                        elif j.type.lower() == "debit":
                            k.debit_cards.append(j)
                            cards.remove(j)
    elif ch == 5:
        for e in customers:
            e.display_customer_info()
    elif ch == 6:
        wc = input("What is the customer name to check cards? ")
        for u in customers:
            if u.name.lower() == wc.lower():
                for t in u.debit_cards:
                    t.display_cards()
                for i in u.credit_cards:
                    i.display_cards()

    elif ch == 7:
        customer_storage = open("customer_storage.dat", "ab")
        card_storage = open("card_storage.dat", "ab")
        for c in customers:
            pickle.dump(c, customer_storage)
        for cd in cards:
            pickle.dump(cd, card_storage)
        customer_storage.close()
        card_storage.close()
    elif ch == 8:
        print("Exiting Program...")
        break
# transfer funds from customer 1 to customer 2