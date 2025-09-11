"""Project: Library Management System (Intermediate OOP Project)
Concepts Covered: Multiple classes, Composition (object inside object), Basic relationships.

Project Description

We'll build a simple Library system where we can:

Create a Book class → attributes: title, author, isbn, available.

Create a Library class → it manages a collection of books.

Add new books.

Display all books.

Borrow a book (mark unavailable).

Return a book (mark available).

Create multiple Book objects and add them into the Library.


"""
class Book:

    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Isbn: {self.isbn}, Available: {self.available}"


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.available:
                    book.available = False
                    print(f"You Borrowed: {book.title}")
                else:
                    print(f"{book.title} is already borrowed.")
                return
        print("Books not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.available:
                    book.available = True
                    print(f"You returned: {book.title}")
                else:
                    print(f"{book.title}: was not borrowed.")
                return
        print("Book not found.")
    
    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book.display_info())


library = Library()

book1 = Book("Python for Everbody", "Dr.Charles", 98765)
book2 = Book("Hands-on ML with scikit-learn", "Geron Aurelien", 76543)
book3 = Book("40 Laws of Power", "Robert Greene", 86775)


library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()

library.borrow_book(86775)

library.display_books()

library.return_book(86775)

library.display_books()
