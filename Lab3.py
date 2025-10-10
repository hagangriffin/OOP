class Book:
    def __init__(self, bid = 0, title = "", author_id = 0, publisher = "", year = ""):
        self.bid = bid
        self.title = title
        self.author_id = author_id
        self.publisher = publisher
        self.year_published = year
    def add_book(self):
        self.bid = int(input("What is the book id? "))
        self.title = input("What is the title? ")
        self.author_id = int(input("What is the author id? "))
        self.publisher = input("Who is the publisher? ")
        self.year_published = input("What year was the book published? ")
        new_book = Book(self.bid, self.title, self.author_id, self.publisher, self.year_published)
        books.append(new_book)
    def display_books(self):
        print("\n| Book ID: ", self.bid, "| Book Title: ", self.title, "| Book Author ID: ", self.author_id, "| Book Publisher: ", self.publisher, "| Year Published: ", self.year_published)
class Author:
    def __init__(self, aid = 0, name = "", affil = "", country = "", phone = "", email = ""):
        self.aid = aid
        self.name = name
        self.affil = affil
        self.country = country
        self.phone = phone
        self.email = email
    def add_author(self):
        self.aid = int(input("What is the author id? "))
        self.name = input("What is the author's name? ")
        self.affil = input("What is the author's affiliation? ")
        self.country = input("What is the author's country? ")
        self.phone = input("What is the author's phone? ")
        self.email = input("What is the author's email? ")
        new_author = Author(self.aid, self.name, self.affil, self.country, self.phone, self.email)
        authors.append(new_author)
    def display_authors(self):
        print("\n| Author ID: ", self.aid, "| Author Name: ", self.name, "| Author Affiliation: ", self.affil, "| Author Country: ", self.country, "| Author Phone: ", self.phone, "| Author Email: ", self.email)
class User:
    def __init__(self, uid = 0, name = "", password = "", address = "", phone = "", email = ""):
        self.uid = uid
        self.name = name
        self.password = password
        self.address = address
        self.phone = phone
        self.email = email
        self.books_borrowed = []
    def add_user(self):
        self.uid = int(input("What is the user id? "))
        self.name = input("What is the user's name? ")
        self.password = input("What is the user's password? ")
        self.address = input("What is the user's address? ")
        self.phone = input("What is the user's phone? ")
        self.email = input("What is the user's email? ")
        new_user = User(self.uid, self.name, self.password, self.address, self.phone, self.email)
        users.append(new_user)

    def borrow_book(self, un):
        book = int(input("What is the id of the book? "))
        found = False
        for j in users:
            if j.uid == un:
                for i in books:
                    if i.bid == book:
                        j.books_borrowed.append(i)
                        print("Book borrowed successfully")
                        found = True
        if not found:
            print("This book does not exist")

    def display_users(self):
        print("\n| User ID: ", self.uid, "| User Name: ", self.name, "| User Password: ", self.password, "| User Address: ", self.address, "| User Phone: ", self.phone, "| User Email: ", self.email)

b1 = Book(1, "Dragon's Lair", 1, "Maximum Publishing", "2005")
b2 = Book(2, "Ghosted", 2, "Perfect Publishing", "2015")
b3 = Book(3, "Cars", 3, "Outreach Publishing", "2008")

a1 = Author(1, "James", "Maximum Publishing", "USA", "1112223333", "james@gmail.com")
a2 = Author(2, "Zach", "Perfect Publishing", "Canada", "4445556666", "zach@gmail.com")
a3 = Author(3, "Brayden", "Outreach Publishing", "China", "7778889999", "brayden@gmail.com")

u1 = User(1, "Hagan", "pass1", "25 Braken Rd", "3332221111", "hagan@gmail.com")
u2 = User(2, "John", "pass2", "12 Country Lp", "6665554444", "john@gmail.com")
u3 = User(3, "Lydia", "pass3", "14 Lazy Dr", "9998887777", "lydia@gmail.com")

books = [b1, b2, b3]
users = [u1, u2, u3]
authors = [a1, a2, a3]

while True:
    print("--------------------------")
    print("\n1. Display Books\n2. Display Authors\n3. Display Users\n4. Add Book\n5. Add Author\n6. Add User\n7. Borrow Book\n8. List Borrowed Books\n9. Exit")
    ch = int(input("What is your choice? "))
    if ch == 1:
        for b in books:
            b.display_books()

    elif ch == 2:
        for a in authors:
            a.display_authors()

    elif ch == 3:
        for u in users:
            u.display_users()

    elif ch == 4:
        new_book = Book()
        new_book.add_book()

    elif ch == 5:
        new_author = Author()
        new_author.add_author()

    elif ch == 6:
        new_user = User()
        new_user.add_user()

    elif ch == 7:
        u = int(input("What is your user id? "))
        u_true = False
        for e in users:
            if e.uid == u:
                e.borrow_book(u)
                u_true = True
        if not u_true:
            print("That user does not exist")

    elif ch == 8:
        us = int(input("What is your user id? "))
        check = False
        for h in users:
            if h.uid == us:
                for z in h.books_borrowed:
                    print(z.title)
                check = True
        if not check:
            print("That user does not exist")
    elif ch == 9:
        print("Exiting Program...")
        break