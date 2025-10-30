class Book:
    
    # Constructor to initialize title, author, and availability status.
    def __init__(self, title, author, available=True):
        self.__title = title
        self.__author = author
        self.__available = available

    # Getter 
    @property
    def get_title(self):
        return self.__title

    # Method to borrow a book
    def borrow_book(self):
        if self.__available:
            self.__available = False
            print(f"You Borrowed: {self.__title}")
        else:
           print(f"{self.__title} is already borrowed.")
           
        return
    
    # Method to return a book
    def return_book(self):
        if not self.__available:
            self.__available = True
            print(f"You Returned: {self.__title}")
        else:
            print(f"{self.__title} was not borrowed.")
    
    def __str__(self):
        status = "Available" if self.__available else "Borrowed"
        return f"{self.__title} - {self.__author} ({status})"
        
    def to_csv(self):
        status = "Available" if self.__available else "Borrowed"
        return f"{self.__title},{self.__author},{status}"

class Library:

    # Constrictor to store books
    def __init__(self):
        self.books = []

    # Add book in list of books
    def add_book(self, book):
        self.books.append(book)

    # Display book info 
    def display_book(self):
        if not self.books:
            print("No book in Library.")
        else:
            for book in self.books:
                print(book)

    # Search book by title
    def search_book(self, title):
        found = False
        for book in self.books:
            if book.get_title.lower() == title.lower(): # accessing private variable
                print("Book Found:", book)
                found = True
                break
        if not found:
            print("Book not found.")

    # Remove book by title
    def remove_book(self, title):
        for book in self.books:
            if book.get_title.lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{title}' removed successfully.")
                return
        print("Book not found.")

    # Load data from file
    def load_from_csv(self, filename):
        with open(filename, "r") as file:
            # Skip the header row
            header = file.readline()

            # Read the remaining lines
            for line in file:
                # Remove leading/trailing whitespace and split by comma
                parts = line.strip().split(",")
        
                # Assign parts to variables, ensuring there are enough elements
                if len(parts) == 3:
                    title, author, available = parts
                    
                    available = available.strip().lower() == "available"
            
                    book = Book(title.strip(), author.strip(), available)
                    self.add_book(book)
def menu():
    library = Library()
    library.load_from_csv("library.csv")

    while True:
        print("\n===== Library Menu =====")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Remove Book")
        print("7. Save & Exit")
        
        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Invalid input. Enter a number between 1-7.")
            continue

        # Add book
        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            book = Book(title, author)
            library.add_book(book)
            print("Book Added Successfully!")
        
        # Display book
        elif choice == 2:
            library.display_book()

        # Search book
        elif choice == 3:
            title = input("Enter title to search: ")
            library.search_book(title)

        # Borrow book
        elif choice == 4:
            title = input("Enter title to Borrow: ")
            found = False
            for book in library.books:
                if book.get_title.lower() == title.lower():
                    book.borrow_book()
                    found = True
                    break
            if not found:
                print("Book not found.")

        # Return book
        elif choice == 5:
            title = input("Enter title to Return: ")
            found = False
            for book in library.books:
                if book.get_title.lower() == title.lower():
                    book.return_book()
                    found = True
                    break
            if not found:
                print("Book not found.")

        # Remove book
        elif choice == 6:
            title = input("Enter title to remove: ")
            library.remove_book(title)

        # Save to file & Exit
        elif choice == 7:
            with open("library.csv", "w") as file:
                file.write("Title,Author,Available\n")
                for b in library.books:
                    file.write(b.to_csv() + "\n")
            print("Library Saved. GoodBye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()