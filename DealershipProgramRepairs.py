import pickle

#Admin Class

class Admin:
    def __init__(self):
        self.inventry = inventory.parts
        self.wait_list = schedule.wait_list
        self.next_job = next(iter(schedule.wait_list.items()))
        self.total_scheduled = schedule.total_scheduled
#Run Invoice Creator
    def create_invoice(self):
        invoice = Invoice()
        invoice.create_invoice()
        invoices.append(invoice)
#Print Inventory
    def check_inventory(self):
        print("\nChecking Inventory...")
        inventory.check_inv()
#Print Schedule
    def check_schedule(self):
        print("\nNext job: ", self.next_job, "\nTotal jobs scheduled: ", self.total_scheduled)

#Invoice Class

class Invoice:
    def __init__(self):
        self.inv_id = 0
        self.name = ""
        self.dob = ""
        self.phone = ""
        self.email = ""
        self.card_name = ""
        self.card_number = ""
        self.card_expiration = ""
        self.card_cvv = ""
        self.car_make = ""
        self.car_model = ""
        self.car_year = ""
        self.car_color = ""
        self.issue = ""
        self.diag_or_repair = ""
        self.est_labor_hrs = 0.0
        self.hrs_per_day = 8
        self.per_hour_pay = 25
        self.total_labor_cost = 0.0
        self.parts_needed = {}
        self.parts_cost = 0.0
        self.total_cost = 0.0
        self.eta_days = 0
#Create Invoice
    def create_invoice(self):
        self.inv_id = input("What is the invoice ID? ")
        self.name = input("What is the customer's name? ")
        self.dob = input("What is the customer's DOB? ")
        self.phone = input("What is the customer's phone? ")
        self.email = input("What is the customer's email? ")
        self.card_number = input("What is the customer's card number? ")
        self.card_name = input("What is the customer's card name? ")
        self.card_expiration = input("What is the customer's card expiration? ")
        self.card_cvv = input("What is the customer's card cvv? ")
        self.car_make = input("What is the customer's car make? ")
        self.car_model = input("What is the customer's car model? ")
        self.car_year = input("What is the customer's car year? ")
        self.car_color =input("What is the customer's car color? ")
        self.issue = input("What is the customer's issue?" )
        self.diag_or_repair = input("Is the invoice for diagnostics or repairs? ")
        self.est_labor_hrs = int(input("What are the estimated labor hours? "))
        self.total_cost = self.labor_calc()
        self.parts_cost = self.parts_calc()
        self.total_cost = self.total_cost_calc()
        self.eta_days = self.eta_calc()

        #Create Invoice Code Here

#Calculate Labor Cost
    def labor_calc(self):
        total_labor_cost = self.per_hour_pay * self.est_labor_hrs
        return total_labor_cost
#Calculate Parts Cost
    def parts_calc(self):
        parts_cost = 0
        for e in self.parts_needed:
            parts_cost += e
        return parts_cost
#Calculate Total Cost
    def total_cost_calc(self):
        total_cost = self.parts_cost + self.total_labor_cost
        return total_cost
#Calculate ETA
    def eta_calc(self):
        eta = self.est_labor_hrs / self.hrs_per_day
        return eta
#Add Invoice to Wait List
    def update_wait_list(self):
        schedule.add_schedule(self.name, self.phone, self.email)

#Inventory Class

class Inventory:
    def __init__(self):
        self.parts = {"Engine Parts": 0, "Drivetrain Parts": 0, "Electronic Parts": 0, "Interior Parts": 0, "Exterior Parts": 0, "Main Frame Parts": 0}
        self.eng_parts_price = 200
        self.drive_parts_price = 125
        self.electro_parts_price = 75
        self.int_parts_price = 100
        self.ext_parts_price = 50
        self.main_frame_parts_price = 175
#Check Inventory Stock
    def check_inv(self):
        print("Total Engine Parts: ", self.parts["Engine Parts"])
        print("Total Drivetrain Parts: ", self.parts["Drivetrain Parts"])
        print("Total Electronic Parts: ", self.parts["Electronic Parts"])
        print("Total Interior Parts: ", self.parts["Interior Parts"])
        print("Total Exterior Parts: ", self.parts["Exterior Parts"])
        print("Total Main Frame Parts: ", self.parts["Main Frame Parts"])
        if self.parts["Engine Parts"] < 10 or self.parts["Drivetrain Parts"] < 10 or self.parts["Electronic Parts"] < 10 or self.parts["Interior Parts"] < 10 or self.parts["Exterior Parts"] < 10 or self.parts["Main Frame Parts"] < 10:
            upd_inv = input("Stock is low. Would you like to order new stock now? ")
            if upd_inv.lower() == "yes":
                print("Auto ordering stock now")
                self.update_inv()
            elif upd_inv.lower() == "no":
                print("Okay, continuing")
            else:
                print("Invalid input")
#Update Inventory Stock
    def update_inv(self):
        order_goal = 50
        stock_ordered = False
        type_ordered = []
        if self.parts["Engine Parts"] < 10:
            eng_parts_ordered = order_goal - self.parts["Engine Parts"]
            print("Engine parts stock low... Ordering more stock\nCost of new stock ordered: ", str(eng_parts_ordered * self.eng_parts_price))
            self.parts["Engine Parts"] += eng_parts_ordered
            stock_ordered = True
            type_ordered.append("Engine Parts")
        elif self.parts["Drivetrain Parts"] < 10:
            dri_parts_ordered = order_goal - self.parts["Drivetrain Parts"]
            print("Drivetrain parts stock low... Ordering more stock\nCost of new stock ordered: ", str(dri_parts_ordered * self.drive_parts_price))
            self.parts["Drivetrain Parts"] += dri_parts_ordered
            stock_ordered = True
            type_ordered.append("Drivetrain Parts")
        elif self.parts["Electronic Parts"] < 10:
            elec_parts_ordered = order_goal - self.parts["Electronic Parts"]
            print("Electronic parts stock low... Ordering more stock\nCost on new stock ordered: ", str(elec_parts_ordered * self.electro_parts_price))
            self.parts["Electronic Parts"] += elec_parts_ordered
            stock_ordered = True
            type_ordered.append("Electronic Parts")
        elif self.parts["Interior Parts"] < 10:
            int_parts_ordered = order_goal - self.parts["Interior Parts"]
            print("Interior parts stock low... Ordering more stock\nCost on new stock ordered: ", str(int_parts_ordered * self.int_parts_price))
            self.parts["Interior Parts"] += int_parts_ordered
            stock_ordered = True
            type_ordered.append("Interior Parts")
        elif self.parts["Exterior Parts"] < 10:
            ext_parts_ordered = order_goal - self.parts["Exterior Parts"]
            print("Exterior parts stock low... Ordering more stock\nCost on new stock ordered: ", str(ext_parts_ordered * self.ext_parts_price))
            self.parts["Exterior Parts"] += ext_parts_ordered
            stock_ordered = True
            type_ordered.append("Exterior Parts")
        elif self.parts["Main Frame Parts"] < 10:
            main_parts_ordered = order_goal - self.parts["Main Frame Parts"]
            print("Main frame parts stock low... Ordering more stock\nCost on new stock ordered: ", str(main_parts_ordered * self.main_frame_parts_price))
            self.parts["Main Frame Parts"] += main_parts_ordered
            stock_ordered = True
            type_ordered.append("Main Frame Parts")

        if stock_ordered:
            print("Types of parts ordered: ", type_ordered)
        elif not stock_ordered:
            print("No parts were needed")

        return self.parts["Engine Parts"], self.parts["Drivetrain Parts"], self.parts["Electronic Parts"], self.parts["Interior Parts"], self.parts["Exterior Parts"], self.parts["Main Frame Parts"]

#Scheduling Class

class Scheduling:
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.email = ""
        self.wait_list = {}
        self.total_scheduled = len(self.wait_list)

#Add to Schedule
    def add_schedule(self, name, phone, email):
        self.wait_list.update({name: {"Phone: ": phone, "Email: ": email}})

#Remove Cancelled Job From Schedule
    def remove_from_schedule(self, name):
        for e in self.wait_list:
            if e.name == name:
                self.wait_list.pop(e)

invoices = []
inventory = Inventory()
schedule = Scheduling()
save_list = {}
loaded_list = {}