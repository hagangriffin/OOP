import pickle
import tkinter as tk
from tkinter import *

#Invoice Class

class Invoice:
    def __init__(self, inv_id = 0, name = "", dob = "", phone = "", email = "", card_name = "", card_number = "", card_expiration = "", card_ccv = "", car_make = "", car_model = "", car_year = "", car_color = "", issue = "", diag_or_repair = "", est_labor = 0):
        self.inv_id = inv_id
        self.name = name
        self.dob = dob
        self.phone = phone
        self.email = email
        self.card_name = card_name
        self.card_number = card_number
        self.card_expiration = card_expiration
        self.card_ccv = card_ccv
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.car_color = car_color
        self.issue = issue
        self.diag_or_repair = diag_or_repair
        self.est_labor_hrs = est_labor
        self.hrs_per_day = 8
        self.per_hour_pay = 25
        self.total_labor_cost = 0.0
        self.parts_needed = {}
        self.parts_cost = 0.0
        self.total_cost = 0.0
        self.eta_days = 0
#Create Invoice
    def create_invoice(self):
        self.inv_id = int(input("What is the invoice ID? "))
        self.name = input("What is the customer's name? ")
        self.dob = input("What is the customer's DOB? ")
        self.phone = input("What is the customer's phone? ")
        self.email = input("What is the customer's email? ")
        self.card_number = input("What is the customer's card number? ")
        self.card_name = input("What is the customer's card name? ")
        self.card_expiration = input("What is the customer's card expiration? ")
        self.card_ccv = input("What is the customer's card cvv? ")
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

        new_inv = Invoice(self.inv_id, self.name, self.dob, self.phone, self.email, self.card_name, self.card_number, self.card_expiration, self.card_ccv, self.car_make, self.car_model, self.car_year, self.car_color, self.issue, self.diag_or_repair, self.est_labor_hrs)
        invoices.append(new_inv)

        dis.insert(tk.INSERT, "Invoice Created")

#Calculate Labor Cost
    def labor_calc(self):
        total_labor_cost = self.per_hour_pay * self.est_labor_hrs
        dis.insert(tk.INSERT, "Calculating Labor Cost...")
        return total_labor_cost

#Calculate Parts Cost
    def parts_calc(self):
        parts_cost = 0
        for e in self.parts_needed:
            parts_cost += e
        dis.insert(tk.INSERT,"Calculating Parts Cost...")
        return parts_cost

#Calculate Total Cost
    def total_cost_calc(self):
        total_cost = self.parts_cost + self.total_labor_cost
        dis.insert(tk.INSERT,"Calculating Total Cost...")
        return total_cost

#Calculate ETA
    def eta_calc(self):
        eta = self.est_labor_hrs / self.hrs_per_day
        return eta

#Add Invoice to Wait List
    def update_wait_list(self):
        schedule.add_schedule(self.name, self.phone, self.email)

    def display_invoices(self):
        dis.insert(tk.INSERT,"--------------------------------------------")
        dis.insert(tk.INSERT, f"Name: {self.name} \nDOB: {self.dob} \nPhone: {self.phone} \nEmail: {self.email} \nCard Name: {self.card_name} \nCard Number: {self.card_number} \nCard Expiry: {self.card_expiration} \nCard CVV: {self.card_ccv} \nCar Make: {self.car_make} \nCar Model: {self.car_model} \nCar Color: {self.car_color} \nCar Year: {self.car_year} \nIssue: {self.issue} \nDiag or Repair: {self.diag_or_repair} \nEstimated Labor Hours: {self.est_labor_hrs}")
        dis.insert(tk.INSERT,"--------------------------------------------")

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
        dis.insert(tk.INSERT,f"Total Engine Parts: {self.parts['Engine Parts']}")
        dis.insert(tk.INSERT,f"\nTotal Drivetrain Parts: {self.parts['Drivetrain Parts']}")
        dis.insert(tk.INSERT,f"\nTotal Electronic Parts: {self.parts['Electronic Parts']}")
        dis.insert(tk.INSERT,f"\nTotal Interior Parts: {self.parts['Interior Parts']}")
        dis.insert(tk.INSERT,f"\nTotal Exterior Parts: {self.parts['Exterior Parts']}")
        dis.insert(tk.INSERT,f"\nTotal Main Frame Parts: {self.parts['Main Frame Parts']}")
        if self.parts["Engine Parts"] < 10 or self.parts["Drivetrain Parts"] < 10 or self.parts["Electronic Parts"] < 10 or self.parts["Interior Parts"] < 10 or self.parts["Exterior Parts"] < 10 or self.parts["Main Frame Parts"] < 10:
            dis.insert(tk.INSERT, "\n\nStock is low... Would you like to order more? Yes/No")

#Update Inventory Stock
    def update_inv(self):
        order_goal = 50
        stock_ordered = False
        type_ordered = []
        total_cost = 0

        if self.parts["Engine Parts"] < 10:
            eng_parts_ordered = order_goal - self.parts["Engine Parts"]
            eng_parts_cost = inventory.eng_parts_price * eng_parts_ordered
            dis.insert(tk.INSERT,f"\n\nEngine parts stock low... Ordering more stock\nCost of new stock ordered: {str(eng_parts_cost)}")
            self.parts["Engine Parts"] += eng_parts_ordered
            stock_ordered = True
            type_ordered.append("Engine Parts")
            total_cost += eng_parts_cost
        if self.parts["Drivetrain Parts"] < 10:
            dri_parts_ordered = order_goal - self.parts["Drivetrain Parts"]
            dri_parts_cost = inventory.drive_parts_price * dri_parts_ordered
            dis.insert(tk.INSERT,f"\n\nDrivetrain parts stock low... Ordering more stock\nCost of new stock ordered: {str(dri_parts_cost)}")
            self.parts["Drivetrain Parts"] += dri_parts_ordered
            stock_ordered = True
            type_ordered.append("Drivetrain Parts")
            total_cost += dri_parts_cost
        if self.parts["Electronic Parts"] < 10:
            elec_parts_ordered = order_goal - self.parts["Electronic Parts"]
            elec_parts_cost = inventory.electro_parts_price * elec_parts_ordered
            dis.insert(tk.INSERT,f"\n\nElectronic parts stock low... Ordering more stock\nCost of new stock ordered: {str(elec_parts_cost)}")
            self.parts["Electronic Parts"] += elec_parts_ordered
            stock_ordered = True
            type_ordered.append("Electronic Parts")
            total_cost += elec_parts_cost
        if self.parts["Interior Parts"] < 10:
            int_parts_ordered = order_goal - self.parts["Interior Parts"]
            int_parts_cost = inventory.int_parts_price * int_parts_ordered
            dis.insert(tk.INSERT,f"\n\nInterior parts stock low... Ordering more stock\nCost of new stock ordered: {str(int_parts_cost)}")
            self.parts["Interior Parts"] += int_parts_ordered
            stock_ordered = True
            type_ordered.append("Interior Parts")
            total_cost += int_parts_cost
        if self.parts["Exterior Parts"] < 10:
            ext_parts_ordered = order_goal - self.parts["Exterior Parts"]
            ext_parts_cost = inventory.ext_parts_price * ext_parts_ordered
            dis.insert(tk.INSERT,f"\n\nExterior parts stock low... Ordering more stock\nCost of new stock ordered: {str(ext_parts_cost)}")
            self.parts["Exterior Parts"] += ext_parts_ordered
            stock_ordered = True
            type_ordered.append("Exterior Parts")
            total_cost += ext_parts_cost
        if self.parts["Main Frame Parts"] < 10:
            main_parts_ordered = order_goal - self.parts["Main Frame Parts"]
            main_parts_cost = inventory.main_frame_parts_price * main_parts_ordered
            dis.insert(tk.INSERT,f"\n\nMain frame parts stock low... Ordering more stock\nCost of new stock ordered: {str(main_parts_cost)}")
            self.parts["Main Frame Parts"] += main_parts_ordered
            stock_ordered = True
            type_ordered.append("Main Frame Parts")
            total_cost += main_parts_cost

        if stock_ordered:
            dis.insert(tk.INSERT, f"\n\nTotal cost of parts ordered: {total_cost}")
            dis.insert(tk.INSERT, "\n\nTypes of parts ordered: ")
            for t in type_ordered:
                dis.insert(tk.INSERT, f"\n{t}")

        elif not stock_ordered:
            dis.insert(tk.INSERT,"\nNo parts were needed")

        return self.parts["Engine Parts"], self.parts["Drivetrain Parts"], self.parts["Electronic Parts"], self.parts["Interior Parts"], self.parts["Exterior Parts"], self.parts["Main Frame Parts"]

#Scheduling Class

class Scheduling:
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.email = ""
        self.wait_list = {}
        self.total_scheduled = len(self.wait_list)

        if len(self.wait_list) > 0:
            self.next_job = next(iter(self.wait_list.items()))

#Add to Schedule
    def add_schedule(self, name = "", phone = "", email = ""):
        self.wait_list.update({self.name: {"Phone: ": self.phone, "Email: ": self.email}})
        dis.insert(tk.INSERT,"Schedule Updated")

#Remove Cancelled Job From Schedule
    def remove_schedule(self):
        sh = input("What is the name of the job to be removed?")
        for n in self.wait_list:
            if n.name == sh:
                self.wait_list.pop(n)
        dis.insert(tk.INSERT,"Job Removed")
#Check Schedule
    def check_schedule(self):
        dis.insert(tk.INSERT,f"Next job: {self.next_job} \nTotal jobs scheduled: {self.total_scheduled}")

inventory = Inventory()
schedule = Scheduling()
invoice = Invoice()
invoices = []
inventories = [inventory]
schedules = [schedule]

#STORAGE-------------------------------------------------------------------------------------

stored_invoices = open("invoices.dat", "ab")
stored_schedule = open("schedule.dat", "ab")
stored_inventory = open("inventory.dat", "ab")

for inv in invoices:
    pickle.dump(inv, stored_invoices)
for sch in schedules:
    pickle.dump(sch, stored_schedule)
for invent in inventories:
    pickle.dump(invent, stored_inventory)

stored_invoices.close()
stored_schedule.close()
stored_inventory.close()

#MAIN MENU------------------------------------------------------------------------------------

top = Tk()
top.geometry("700x500")

dis = Text(width=60, height=15)
dis.place(x=100, y=100)

def show(x):
    try:
        if x == "ci":
            invoice.create_invoice()
        elif x == "cin":
            inventory.check_inv()
        elif x == "csh":
            schedule.check_schedule()
        elif x == "yes":
            inventory.update_inv()
        elif x == "no":
            dis.insert(tk.INSERT, "\n\nContinuing...")
    except:
        dis.insert(tk.INSERT, "\n\nInvalid Input")

cr_in = Button(top, text="Create Invoice", width=10, height=5, command=lambda: show("ci"))
cr_in.place(x=110, y=375)
ch_in = Button(top, text="Check Inventory", width=10, height=5, command=lambda: show("cin"))
ch_in.place(x=205, y=375)
ch_sh = Button(top, text="Check Schedule", width=10, height=5, command=lambda: show("csh"))
ch_sh.place(x=300, y=375)
yes = Button(top, text="Yes", width=10, height=5, command=lambda: show("yes"))
yes.place(x=395, y=375)
no = Button(top, text="No", width=10, height=5, command=lambda: show("no"))
no.place(x=490, y=375)

top.mainloop()