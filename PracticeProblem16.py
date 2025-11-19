import pickle

class Product:
    def __init__(self, pid = "", pname = "", price = 0.0, pdesc = ""):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.pdesc = pdesc

    def new_prod_det(self):
        self.pid = input("What is the pid?")
        self.pname = input("What is the product name?")
        self.price = float(input("What is the product price?"))
        self.pdesc = input("What is the product description?")
        new_p = Product(self.pid, self.pname, self.price, self.pdesc)
        products.append(new_p)

    def display_prod(self):
        print("PID: ", self.pid, "Product Name: ", self.pname, "Product Price: ", self.price, "Product Description: ", self.pdesc)

products = []

while True:
    print("1. Add Product\n2. Update Product\n3. Display Product\n4. Write to File\n5. Read from File")
    i = int(input("What is your choice"))
    if i == 1:
        new_p = Product()
        new_p.new_prod_det()

    elif i == 2:

    elif i == 3:

    elif i == 4:

    elif i == 5