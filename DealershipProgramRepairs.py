class Admin:
    def __init__(self):
        invntry = []
        invoice = "invoice"
        wait_list = []
        next_job = "next job"
        total_scheduled = 0

    def create_invoice(self):

    def check_inventory(self):

    def check_schedule(self):

    def total_schedules(self):

class Invoice:
    def __init__(self):
        inv_id = 0
        name = "name"
        dob = "dob"
        contact = {}
        card_info = {}
        car_details = {}
        issue = "issue"
        diag_or_repair = "input"
        est_labor_hrs = 0.0
        per_hour_pay = 0.0
        total_labor_cost = 0.0
        parts_needed = []
        parts_cost = 0.0
        eta_days = 0

    def create_invoice(self):

    def labor_calc(self):

    def parts_calc(self):

    def total_cost_calc(self):

    def update_wait_list(self):

class Inventory:
    def __init__(self):
        eng_parts = {}
        drive_parts = {}
        electro_parts = {}
        int_parts = {}
        ext_parts = {}
        main_frame_parts = {}

    def check_inv(self):

    def order_stock(self):

    def update_inv(self):

class Scheduling:
    def __init__(self):
        name = "name"
        contact = {}
        next_job_info = "next"
        total_scheduled = 0

    def add_schedule(self):

    def bump_schedule(self):

    def remove_schedule(self):

    def total_scheduled(self):