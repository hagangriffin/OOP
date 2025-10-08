class Admin:
    def __init__(self):
        self.invntry = []
        self.wait_list = []
        self.next_job = ""
        self.total_scheduled = 0

    def create_invoice(self):
        invoice = Invoice()
        return invoice
    def check_inventory(self):
        print("Checking Inventory...")
        inventory.check_inv()
    def check_schedule(self):

    def total_scheduled(self):

class Invoice:
    def __init__(self):
        self.inv_id = 0
        self.name = ""
        self.dob = ""
        self.contact = {}
        self.card_info = {}
        self.car_details = {}
        self.issue = ""
        self.diag_or_repair = ""
        self.est_labor_hrs = 0.0
        self.per_hour_pay = 25
        self.total_labor_cost = 0.0
        self.parts_needed = {}
        self.parts_cost = 0.0
        self.total_cost = 0.0
        self.eta_days = 0

    def create_invoice(self):

    def labor_calc(self):
        self.total_labor_cost = self.per_hour_pay * self.est_labor_hrs
    def parts_calc(self):
        for e in self.parts_needed:
            self.parts_cost += e
        return self.parts_cost
    def total_cost_calc(self):
        self.total_cost = self.parts_cost + self.total_labor_cost
    def update_wait_list(self):
        schedule.add_schedule()
class Inventory:
    def __init__(self):
        self.eng_parts = 0
        self.drive_parts = 0
        self.electro_parts = 0
        self.int_parts = 0
        self.ext_parts = 0
        self.main_frame_parts = 0

    def check_inv(self):
        print("Total Engine Parts: ", self.eng_parts)
        print("Total Drivetrain Parts: ", self.drive_parts)
        print("Total Electronic Parts: ", self.electro_parts)
        print("Total Interior Parts: ", self.int_parts)
        print("Total Exterior Parts: ", self.ext_parts)
        print("Total Main Frame Parts: ", self.main_frame_parts)
        order_goal = 50
        need_stock = False
        if self.eng_parts < 10:
            print("Engine parts stock low... Ordering more stock\nCost of new stock ordered: ", variable)
            self.eng_parts += order_goal - self.eng_parts
        elif self.drive_parts < 10:
            print("Drivetrain parts stock low... Ordering more stock\nCost of new stock ordered: ", variable)
            self.drive_parts += order_goal - self.drive_parts
        elif self.electro_parts < 10:
            print("Electronic parts stock low... Ordering more stock\nCost on new stock ordered: ", variable)
            self.electro_parts += order_goal - self.electro_parts
        elif self.int_parts < 10:
            print("Interior parts stock low... Ordering more stock\nCost on new stock ordered: ", variable)
            self.int_parts += order_goal - self.int_parts
        elif self.ext_parts < 10:
            print("Exterior parts stock low... Ordering more stock\nCost on new stock ordered: ", variable)
            self.ext_parts += order_goal - self.ext_parts
        elif self.main_frame_parts < 10:
            print("Main frame parts stock low... Ordering more stock\nCost on new stock ordered: ", variable)
            self.main_frame_parts += order_goal - self.main_frame_parts

        if not need_stock:
            print("All stock is adequate")
        elif need_stock:
            print("All stock is now ordered")
    def update_inv(self):

class Scheduling:
    def __init__(self):
        self.name = ""
        self.contact = {}
        self.wait_list = {}
        self.total_scheduled = 0

    def add_schedule(self):
        self.wait_list.update({self.name: {"Contact Info: ": self.contact}})
    def bump_schedule(self):

    def remove_schedule(self):

    def total_scheduled(self):
        for e in self.wait_list:
            self.total_scheduled += 1

inventory = Inventory()
schedule = Scheduling()