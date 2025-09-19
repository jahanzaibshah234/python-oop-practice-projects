# Student Record Management System with File Handling

## Concepts Covered

- Encapsulation with private attributes
- Getter and setter methods with validation
- File handling (read/write operations)
- CRUD operations with persistent storage

## Project Description

This Python application is a comprehensive Student Record Management System, extending the Student Grade Management concept with robust file handling and persistent data storage. The system allows users to manage student records using a CSV file and provides all essential CRUD (Create, Read, Update, Delete) operations.

### Features

1. **Encapsulated Student Class**
    - Private attributes: `__name`, `__roll_number`, `__grade`
    - Getter and setter methods for safe data access and validation

2. **Persistent Storage**
    - All student records are saved to a CSV file (`students.csv`)
    - New student entries are appended to the file

3. **Read & Display Records**
    - Program reads from the CSV file and displays all student records

4. **Search Functionality**
    - Users can search for a student by roll number
    - If found, the student's complete record is displayed

5. **Update Records**
    - Users can update a student's grade:
        - System reads all students from the file
        - Updates the specified student's grade
        - Saves all records back to the file

6. **Delete Records**
    - Users can delete a student record by roll number
    - System updates the CSV file after deletion

### What You'll Learn

- How to use private attributes and encapsulation in Python classes
- How to implement property-based getters and setters with validation
- How to perform file input/output operations with CSV files
- How to build a CRUD application with persistent storage

---

This project is ideal for learners who want to combine OOP principles with practical file handling and persistent data management in Python!
