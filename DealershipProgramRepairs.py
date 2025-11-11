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
#Create Invoice Calcs
    def invoice_calc(self):
        self.total_cost = self.labor_calc()
        self.parts_cost = self.parts_calc()
        self.total_cost = self.total_cost_calc()
        self.eta_days = self.eta_calc()
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
        inv_dis.delete("1.0", tk.END)
        inv_dis.insert(tk.INSERT,"--------------------------------------------")
        inv_dis.insert(tk.INSERT, f"\nName: {self.name} \nDOB: {self.dob} \nPhone: {self.phone} \nEmail: {self.email} \nCard Name: {self.card_name} \nCard Number: {self.card_number} \nCard Expiry: {self.card_expiration} \nCard CVV: {self.card_ccv} \nCar Make: {self.car_make} \nCar Model: {self.car_model} \nCar Color: {self.car_color} \nCar Year: {self.car_year} \nIssue: {self.issue} \nDiag or Repair: {self.diag_or_repair} \nEstimated Labor Hours: {self.est_labor_hrs}")
        inv_dis.insert(tk.INSERT,"\n--------------------------------------------")

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
        int_dis.insert(tk.INSERT,f"Total Engine Parts: {self.parts['Engine Parts']}")
        int_dis.insert(tk.INSERT,f"\nTotal Drivetrain Parts: {self.parts['Drivetrain Parts']}")
        int_dis.insert(tk.INSERT,f"\nTotal Electronic Parts: {self.parts['Electronic Parts']}")
        int_dis.insert(tk.INSERT,f"\nTotal Interior Parts: {self.parts['Interior Parts']}")
        int_dis.insert(tk.INSERT,f"\nTotal Exterior Parts: {self.parts['Exterior Parts']}")
        int_dis.insert(tk.INSERT,f"\nTotal Main Frame Parts: {self.parts['Main Frame Parts']}")
        if self.parts["Engine Parts"] < 10 or self.parts["Drivetrain Parts"] < 10 or self.parts["Electronic Parts"] < 10 or self.parts["Interior Parts"] < 10 or self.parts["Exterior Parts"] < 10 or self.parts["Main Frame Parts"] < 10:
            int_dis.insert(tk.INSERT, """\n\nStock is low... To order more click "Update Inventory" """)
        else:
            int_dis.insert(tk.INSERT, "Stock is up to date...")

#Update Inventory Stock
    def update_inv(self):
        order_goal = 50
        stock_ordered = False
        type_ordered = []
        total_cost = 0

        if self.parts["Engine Parts"] < 10:
            eng_parts_ordered = order_goal - self.parts["Engine Parts"]
            eng_parts_cost = inventory.eng_parts_price * eng_parts_ordered
            int_dis.insert(tk.INSERT,f"\n\nEngine parts stock low... Ordering more stock\nCost of new stock ordered: {str(eng_parts_cost)}")
            self.parts["Engine Parts"] += eng_parts_ordered
            stock_ordered = True
            type_ordered.append("Engine Parts")
            total_cost += eng_parts_cost
        if self.parts["Drivetrain Parts"] < 10:
            dri_parts_ordered = order_goal - self.parts["Drivetrain Parts"]
            dri_parts_cost = inventory.drive_parts_price * dri_parts_ordered
            int_dis.insert(tk.INSERT,f"\n\nDrivetrain parts stock low... Ordering more stock\nCost of new stock ordered: {str(dri_parts_cost)}")
            self.parts["Drivetrain Parts"] += dri_parts_ordered
            stock_ordered = True
            type_ordered.append("Drivetrain Parts")
            total_cost += dri_parts_cost
        if self.parts["Electronic Parts"] < 10:
            elec_parts_ordered = order_goal - self.parts["Electronic Parts"]
            elec_parts_cost = inventory.electro_parts_price * elec_parts_ordered
            int_dis.insert(tk.INSERT,f"\n\nElectronic parts stock low... Ordering more stock\nCost of new stock ordered: {str(elec_parts_cost)}")
            self.parts["Electronic Parts"] += elec_parts_ordered
            stock_ordered = True
            type_ordered.append("Electronic Parts")
            total_cost += elec_parts_cost
        if self.parts["Interior Parts"] < 10:
            int_parts_ordered = order_goal - self.parts["Interior Parts"]
            int_parts_cost = inventory.int_parts_price * int_parts_ordered
            int_dis.insert(tk.INSERT,f"\n\nInterior parts stock low... Ordering more stock\nCost of new stock ordered: {str(int_parts_cost)}")
            self.parts["Interior Parts"] += int_parts_ordered
            stock_ordered = True
            type_ordered.append("Interior Parts")
            total_cost += int_parts_cost
        if self.parts["Exterior Parts"] < 10:
            ext_parts_ordered = order_goal - self.parts["Exterior Parts"]
            ext_parts_cost = inventory.ext_parts_price * ext_parts_ordered
            int_dis.insert(tk.INSERT,f"\n\nExterior parts stock low... Ordering more stock\nCost of new stock ordered: {str(ext_parts_cost)}")
            self.parts["Exterior Parts"] += ext_parts_ordered
            stock_ordered = True
            type_ordered.append("Exterior Parts")
            total_cost += ext_parts_cost
        if self.parts["Main Frame Parts"] < 10:
            main_parts_ordered = order_goal - self.parts["Main Frame Parts"]
            main_parts_cost = inventory.main_frame_parts_price * main_parts_ordered
            int_dis.insert(tk.INSERT,f"\n\nMain frame parts stock low... Ordering more stock\nCost of new stock ordered: {str(main_parts_cost)}")
            self.parts["Main Frame Parts"] += main_parts_ordered
            stock_ordered = True
            type_ordered.append("Main Frame Parts")
            total_cost += main_parts_cost

        if stock_ordered:
            int_dis.insert(tk.INSERT, f"\n\nTotal cost of parts ordered: {total_cost}")
            int_dis.insert(tk.INSERT, "\n\nTypes of parts ordered: ")
            for t in type_ordered:
                int_dis.insert(tk.INSERT, f"\n{t}")

        elif not stock_ordered:
            int_dis.insert(tk.INSERT,"\nNo parts were needed")

        return self.parts["Engine Parts"], self.parts["Drivetrain Parts"], self.parts["Electronic Parts"], self.parts["Interior Parts"], self.parts["Exterior Parts"], self.parts["Main Frame Parts"]

#Scheduling Class

class Scheduling:
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.email = ""
        self.wait_list = {}
        self.total_scheduled = 0
        self.next_job = ""

#Add to Schedule
    def add_schedule(self, name, phone, email):
        self.wait_list.update({name: {"Phone: ": phone, "Email: ": email}})
        dis.insert(tk.INSERT,"Schedule Updated...")

#Remove Cancelled Job From Schedule
    def remove_schedule(self, x):
        for n in self.wait_list:
            if n.name == x:
                self.wait_list.pop(n)
        dis.insert(tk.INSERT,"Job Removed")
#Check Schedule
    def check_schedule(self):
        self.total_scheduled = len(self.wait_list)
        if len(self.wait_list) > 0:
            self.next_job = next(iter(self.wait_list.items()))
        sch_dis.insert(tk.INSERT,f"Next job: {self.next_job} \nTotal jobs scheduled: {self.total_scheduled}")

def create_invoice(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10,
                           entry11, entry12, entry13, entry14, entry15, entry16):
    inv_id = entry1
    name = entry2
    dob = entry3
    phone = entry4
    email = entry5
    card_number = entry6
    card_name = entry7
    card_expiration = entry8
    card_ccv = entry9
    car_make = entry10
    car_model = entry11
    car_year = entry12
    car_color = entry13
    issue = entry14
    diag_or_repair = entry15
    est_labor_hrs = int(entry16)

    new_inv = Invoice(inv_id, name, dob, phone, email, card_name,
                              card_number, card_expiration, card_ccv, car_make, car_model,
                              car_year, car_color, issue, diag_or_repair, est_labor_hrs)
    new_inv.invoice_calc()
    invoices.append(new_inv)

    inv_dis.delete("1.0", tk.END)
    inv_dis.insert(tk.INSERT, "Invoice Created")

invent = Invoice(1,"2","3","4","5","6","7","8","9","10","11","12","13","14","15",16)

inventory = Inventory()
schedule = Scheduling()
invoice = Invoice()
invoices = [invent]
inventories = [inventory]
schedules = [schedule]

#MAIN MENU--------------------------------------------------------------------------------------------------------------

top = Tk()
top.geometry("700x500")

dis = Text(width=60, height=15)
dis.place(x=100, y=50)

#SCHEDULE WINDOW--------------------------------------------------------------------------------------------------------
sch = tk.Toplevel(top)
sch.geometry("700x500")
sch.title("Scheduling")

sch_dis = Text(sch, width=60, height=15)
sch_dis.place(x=100, y=50)

sch_ent = Entry(sch, width=60)
sch_ent.place(x=100, y=305)

sch.withdraw()

def schedule_window():

    sch.deiconify()

    def sch_show(x):
        if x == "csh":
            schedule.check_schedule()

        elif x == "addsh":
            sch_creator()

        elif x == "remsh":
            sch_dis.insert(tk.INSERT, """Enter the name to be removed from schedule\nthen click "Submit" """)

        elif x == "exit":
            top.deiconify()
            sch.withdraw()

        elif x == "sub":
            get_ent = sch_ent.get()
            schedule.remove_schedule(get_ent)
            top.deiconify()
            sch.withdraw()

    ch_sh = Button(sch, text="Check Schedule", width=20, height=2, command=lambda: sch_show("csh"))
    ch_sh.place(x=100, y=330)
    add_sh = Button(sch, text="Add to Schedule", width=20, height=2, command=lambda: sch_show("addsh"))
    add_sh.place(x=100, y=380)
    rem_sh = Button(sch, text="Remove from Schedule", width=20, height=2, command=lambda: sch_show("remsh"))
    rem_sh.place(x=260, y=330)
    ex = Button(sch, text="Exit", width=15, height=2, command=lambda: sch_show("exit"))
    ex.place(x=260, y=380)
    sub = Button(sch, text="Submit", width=10, height=1, command=lambda: sch_show("sub"))
    sub.place(x=478, y=298)

#INVOICES WINDOW--------------------------------------------------------------------------------------------------------
inv_wind = tk.Toplevel(top)
inv_wind.geometry("700x500")
inv_wind.title("Invoices")

inv_dis = Text(inv_wind, width=60, height=15)
inv_dis.place(x=100, y=50)

inv_wind.withdraw()

def invoices_window():

    inv_wind.deiconify()

    inv_ent = Entry(inv_wind, width=60)
    inv_ent.place(x=100, y=300)

    def inv_show(x):
        if x == "crin":
            inv_create_win()
            inv_wind.withdraw()
        elif x == "show":
            if len(invoices) > 0:
                for e in invoices:
                    e.display_invoices()
            else:
                inv_dis.insert(tk.INSERT, "\nNo invoices currently saved...")
        elif x == "del":
            inv_dis.delete("1.0", tk.END)
            inv_dis.insert(tk.INSERT, "Enter the name on the invoice in the entry box below then \nclick submit...")
        elif x == "submit":
            nm = inv_ent.get()
            inv_ent.delete(0, tk.END)
            if len(invoices) > 0:
                for e in invoices:
                    if e.name.lower() == nm.lower():
                        invoices.remove(e)
                        inv_dis.insert(tk.INSERT, f"""\nInvoice matching name "{nm}" deleted...""")
                    else:
                        inv_dis.insert(tk.INSERT, f"""\nNo invoice found matching name "{nm}"... """)
            elif len(invoices) == 0:
                inv_dis.insert(tk.INSERT, "\nNo invoices currently saved...")

        elif x == "exit":
            top.deiconify()
            inv_wind.withdraw()

    cr_in = Button(inv_wind, text="Create Invoice", width=20, height=2, command=lambda: inv_show("crin"))
    cr_in.place(x=100, y=325)

    sh_in = Button(inv_wind, text="Show Invoices", width=20, height=2, command=lambda: inv_show("show"))
    sh_in.place(x=100, y=375)

    del_in = Button(inv_wind, text="Delete Invoice", width=20, height=2, command=lambda: inv_show("del"))
    del_in.place(x=260, y=325)

    exit_in = Button(inv_wind, text="Exit", width=15, height=2, command=lambda: inv_show("exit"))
    exit_in.place(x=260, y=375)

    submit = Button(inv_wind, text="Submit", width=12, height=1, command=lambda: inv_show("submit"))
    submit.place(x=478, y=298)

#INVENTORY WINDOW-------------------------------------------------------------------------------------------------------
int_men = tk.Toplevel(top)
int_men.geometry("700x500")
int_men.title("Inventory")

int_dis = Text(int_men, width=60, height=15)
int_dis.place(x=100, y=50)

int_men.withdraw()

def inventory_menu():

    int_men.deiconify()

    def int_show(x):
        if x == "intcheck":
            inventory.check_inv()

        elif x == "upint":
            inventory.update_inv()

        elif x == "exit":
            int_men.withdraw()
            top.deiconify()

    int_check = Button(int_men, text="Check Inventory", width=20, height=2, command=lambda: int_show("intcheck"))
    int_check.place(x=100, y=305)

    int_exit = Button(int_men, text="Exit", width=15, height=2, command=lambda: int_show("exit"))
    int_exit.place(x=100, y=355)

    int_update = Button(int_men, text="Update Inventory", width=20, height=2, command=lambda: int_show("upint"))
    int_update.place(x=260, y=305)

#INVOICE CREATOR WINDOW-------------------------------------------------------------------------------------------------
top1 = tk.Toplevel(top)
top1.title("Invoice Creation")
top1.geometry("500x575")

top1.withdraw()

def inv_create_win():

    top1.deiconify()

    def cr_i():
        create_invoice(inv_id_entry.get(), name_entry.get(), dob_entry.get(), phone_entry.get(), email_entry.get(), card_num_entry.get(),
                               card_name_entry.get(), card_exp_entry.get(), card_cvv_entry.get(), car_make_entry.get(), car_model_entry.get(),
                               car_year_entry.get(), car_color_entry.get(), issue_entry.get(), diag_repair_entry.get(), labor_hours_entry.get())
        top1.withdraw()
        inv_wind.deiconify()

    tk.Label(top1, text="Invoice ID:").place(x=10, y=10)
    inv_id_entry = Entry(top1, width=60)
    inv_id_entry.place(x=125, y=12)

    tk.Label(top1, text="Name:").place(x=10, y=40)
    name_entry = Entry(top1, width=60)
    name_entry.place(x=125, y=42)

    tk.Label(top1, text="DOB:").place(x=10, y=70)
    dob_entry = Entry(top1, width=60)
    dob_entry.place(x=125, y=72)

    tk.Label(top1, text="Phone:").place(x=10, y=100)
    phone_entry = Entry(top1, width=60)
    phone_entry.place(x=125, y=102)

    tk.Label(top1, text="Email:").place(x=10, y=130)
    email_entry = Entry(top1, width=60)
    email_entry.place(x=125, y=132)

    tk.Label(top1, text="Card Number:").place(x=10, y=160)
    card_num_entry = Entry(top1, width=60)
    card_num_entry.place(x=125, y=162)

    tk.Label(top1, text="Card Name:").place(x=10, y=190)
    card_name_entry = Entry(top1, width=60)
    card_name_entry.place(x=125, y=192)

    tk.Label(top1, text="Card Expiration:").place(x=10, y=220)
    card_exp_entry = Entry(top1, width=60)
    card_exp_entry.place(x=125, y=222)

    tk.Label(top1, text="Card CVV:").place(x=10, y=250)
    card_cvv_entry = Entry(top1, width=60)
    card_cvv_entry.place(x=125, y=252)

    tk.Label(top1, text="Car Make:").place(x=10, y=280)
    car_make_entry = Entry(top1, width=60)
    car_make_entry.place(x=125, y=282)

    tk.Label(top1, text="Car Model:").place(x=10, y=310)
    car_model_entry = Entry(top1, width=60)
    car_model_entry.place(x=125, y=312)

    tk.Label(top1, text="Car Year:").place(x=10, y=340)
    car_year_entry = Entry(top1, width=60)
    car_year_entry.place(x=125, y=342)

    tk.Label(top1, text="Car Color:").place(x=10, y=370)
    car_color_entry = Entry(top1, width=60)
    car_color_entry.place(x=125, y=372)

    tk.Label(top1, text="Issue:").place(x=10, y=400)
    issue_entry = Entry(top1, width=60)
    issue_entry.place(x=125, y=402)

    tk.Label(top1, text="Diagnosis or Repair:").place(x=10, y=430)
    diag_repair_entry = Entry(top1, width=60)
    diag_repair_entry.place(x=125, y=432)

    tk.Label(top1, text="Est. Labor Hours:").place(x=10, y=460)
    labor_hours_entry = Entry(top1, width=60)
    labor_hours_entry.place(x=125, y=462)

    submit = Button(top1, text="Submit", width=20, height=2, command=cr_i)
    submit.place(x=175, y=500)

#SCHEDULE CREATOR-------------------------------------------------------------------------------------------------------

sh_cr = tk.Toplevel(top)
sh_cr.geometry("500x150")
sh_cr.title("Schedule Creation")

sh_cr.withdraw()

def sch_creator():

    sh_cr.deiconify()

    def sh_show(x):
        if x == "sub":
            cr_s()

    def cr_s():
        schedule.add_schedule(name_entry.get(), phone_entry.get(), email_entry.get())

        sh_cr.withdraw()
        top.deiconify()

    tk.Label(sh_cr, text="Name").place(x=10, y=10)
    name_entry = Entry(sh_cr, width=60)
    name_entry.place(x=125, y=12)

    tk.Label(sh_cr, text="Phone").place(x=10, y=40)
    phone_entry = Entry(sh_cr, width=60)
    phone_entry.place(x=125, y=42)

    tk.Label(sh_cr, text="Email").place(x=10, y=70)
    email_entry = Entry(sh_cr, width=60)
    email_entry.place(x=125, y=72)

    submit = Button(sh_cr, text="Submit", width=20, height=1, command=lambda: sh_show("sub"))
    submit.place(x=175, y=102)

#MAIN WINDOW BUTTONS----------------------------------------------------------------------------------------------------

def show(x):
    try:
        if x == "ci":
            invoices_window()
            top.withdraw()

        elif x == "cin":
            inventory_menu()
            top.withdraw()

        elif x == "sch":
            schedule_window()
            top.withdraw()

        elif x == "save":
            dis.insert(tk.INSERT, "Saving...\nSaved...")
            stored_invoices = open("invoices.dat", "ab")
            stored_schedule = open("schedule.dat", "ab")
            stored_inventory = open("inventory.dat", "ab")

            stored_invoices.seek(0)
            stored_invoices.truncate()
            stored_schedule.seek(0)
            stored_schedule.truncate()
            stored_inventory.seek(0)
            stored_inventory.truncate()

            for inv in invoices:
                pickle.dump(inv, stored_invoices)
            for sch in schedules:
                pickle.dump(sch, stored_schedule)
            for invent in inventories:
                pickle.dump(invent, stored_inventory)

            stored_invoices.close()
            stored_schedule.close()
            stored_inventory.close()

        elif x == "load":

            dis.insert(tk.INSERT, "Loading...\nLoaded...")
            stored_invoices = open("invoices.dat", "ab")
            stored_schedule = open("schedule.dat", "ab")
            stored_inventory = open("inventory.dat", "ab")

            while True:

                try:
                    loaded_invoices = pickle.load(stored_invoices)
                    count = len(invoices)
                    while count != 0:
                        invoices.pop()
                        count -= 1

                    for e in loaded_invoices:
                        invoices.append(e)

                    dis.insert(tk.INSERT, "Invoices Loaded...")

                except EOFError:
                    continue

                try:
                    loaded_schedule = pickle.load(stored_schedule)
                    schedules.pop()
                    schedules.append(loaded_schedule)

                    dis.insert(tk.INSERT, "Schedule Loaded...")

                except EOFError:
                    continue

                try:
                    loaded_inventory = pickle.load(stored_inventory)
                    inventories.pop()
                    inventories.append(loaded_inventory)

                    dis.insert(tk.INSERT, "Inventory Loaded...")

                except EOFError:
                    continue
        elif x == "exit":
            top.quit()

    except:
        dis.insert(tk.INSERT, "\n\nInvalid Input")

inv_men = Button(top, text="Invoice Menu", width=20, height=2, command=lambda: show("ci"))
inv_men.place(x=110, y=305)
ch_in = Button(top, text="Inventory Menu", width=20, height=2, command=lambda: show("cin"))
ch_in.place(x=110, y=355)
sh = Button(top, text="Scheduling Menu", width=20, height=2, command=lambda: show("sch"))
sh.place(x=110, y=405)

save = Button(top, text="Save", width=15, height=2, command=lambda: show("save"))
save.place(x=270, y=305)
load = Button(top, text="Load", width=15, height=2, command=lambda: show("load"))
load.place(x=270, y=355)
exi = Button(top, text="Exit", width=15, height=2, command=lambda: show("exit"))
exi.place(x=270, y=405)

top.mainloop()