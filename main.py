class Library:
    def __init__(self):
        self.books = {}  # Store book title and quantity
        self.issued_books = {}  # Store book and borrower information

    def add_book(self, title, quantity):
        if title in self.books:
            self.books[title] += quantity
        else:
            self.books[title] = quantity
        print(f"'{title}' has been added with quantity {quantity}.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Available Books:")
            for title, qty in self.books.items():
                print(f"- {title}: {qty} copies")
        print()

    def issue_book(self, title, borrower):
        if title not in self.books or self.books[title] == 0:
            print(f"'{title}' is not available for issuing.")
        else:
            self.books[title] -= 1
            self.issued_books[borrower] = title
            print(f"'{title}' has been issued to {borrower}.")

    def return_book(self, borrower):
        if borrower not in self.issued_books:
            print(f"No book issued under the name {borrower}.")
        else:
            title = self.issued_books.pop(borrower)
            self.books[title] += 1
            print(f"'{title}' has been returned by {borrower}.")

def menu():
    library = Library()
    while True:
        print("~~~~~~~~ Library Management System ~~~~~~~~")
        print("1. Add Book")
        print("2. Display Available Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            quantity = int(input("Enter quantity: "))
            library.add_book(title, quantity)
        elif choice == '2':
            library.display_books()
        elif choice == '3':
            title = input("Enter book title: ")
            borrower = input("Enter borrower name: ")
            library.issue_book(title, borrower)
        elif choice == '4':
            borrower = input("Enter borrower name: ")
            library.return_book(borrower)
        elif choice == '5':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
            
menu()
