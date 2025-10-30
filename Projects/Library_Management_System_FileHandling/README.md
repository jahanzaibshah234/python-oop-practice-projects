# Library Management System with File Handling

## Concepts Covered
- Encapsulation with private attributes
- Property-based getters for safe access
- Methods with internal state validation (borrow/return)
- File handling (CSV read/write operations)
- CRUD operations with persistent storage
- Simple CLI menu-driven interaction

## Project Description
This Python application is a lightweight Library Management System that demonstrates object-oriented design and persistent storage using CSV files. It provides a Book class with encapsulated attributes and a Library class to manage a collection of books. The system supports adding, listing, searching, borrowing, returning, removing books, and saving the library state to a `library.csv` file.

The CLI menu offers an easy way to interact with the library and persists changes between runs by reading from and writing to a CSV file.

## Features

Encapsulated Book class
- Private attributes: `__title`, `__author`, `__available`
- Property-based getter for the title
- Borrow and return methods that enforce availability rules
- `__str__` for readable display
- `to_csv()` to serialize a book to CSV format

Library manager
- Stores `Book` objects in-memory in a list
- Add books to the library
- Display all books (with availability status)
- Search a book by title (case-insensitive)
- Borrow and return operations that update book availability
- Remove a book by title
- Load from and save to `library.csv` for persistent storage

Persistent storage
- On start, the program loads books from `library.csv` (if present)
- On exit, the program writes all current books to `library.csv` with the header:
  `Title,Author,Available`

CLI Menu
- Add Book
- Display Books
- Search Book
- Borrow Book
- Return Book
- Remove Book
- Save & Exit

## File Format (library.csv)
The CSV file must use the following header as the first line:
```
Title,Author,Available
```
Each record follows the header and uses `Available` or `Borrowed` for the availability column, for example:
```
The Hobbit,J.R.R. Tolkien,Available
1984,George Orwell,Borrowed
```

## How to Use

1. Save the provided code into a file named `library.py`.
2. (Optional) Create `library.csv` in the same folder with the header and any initial books.
3. Run the program:
```
python library.py
```
4. Use the numeric menu to interact with the library.
5. When you choose "Save & Exit" the program writes the current library to `library.csv`.

## Example library.csv
```
Title,Author,Available
The Hobbit,J.R.R. Tolkien,Available
To Kill a Mockingbird,Harper Lee,Borrowed
```

## Example Session
- Start program -> it loads existing `library.csv`.
- Choose "1. Add Book": enter title and author -> book added (default Available).
- Choose "2. Display Books": see list and status.
- Choose "4. Borrow Book": provide title -> status changes to Borrowed if it was Available.
- Choose "7. Save & Exit": writes the current list back to `library.csv`.

## What You'll Learn
- How to use private attributes to encapsulate state in Python classes
- How to expose safe, read-only access via properties
- How to implement simple state-changing methods with validation (borrow/return)
- How to persist objects to CSV and load them back
- How to design a small CRUD application with a simple CLI

## License
This project is provided as-is for learning and educational purposes. Feel free to adapt it for your own use.
