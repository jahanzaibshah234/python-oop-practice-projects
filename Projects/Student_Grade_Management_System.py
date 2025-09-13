"""Project: Student Grade Management System

Concepts Covered:

Encapsulation (private attributes with __)

Getters & Setters (@property)

Data validation

Class interaction

Project Description

We'll create a system where:

A Student class has private attributes → __name, __roll_number, __grade.

Use getter and setter methods to control access to grade.

Validate grade (must be between 0 and 100).

A method to check if the student passed or failed.

A small demo to show multiple students.

"""
# Parent class
class Student:

    # Constructor
    def __init__(self, name, roll_number, grade):
        self.__name = name
        self.__roll_number = roll_number
        self.grade = grade

    # Getter method
    @property
    def name(self):
        return self.__name
    
    @property
    def roll_number(self):
        return self.__roll_number

    @property
    def grade(self):
        return self.__grade
    
    # Setter method
    @grade.setter
    def grade(self, value):
        if 0 <= value <= 100:
            self.__grade = value
            
        else:
            self.__grade = 0
            print("Invalid grade. Must be between 0 and 100.")


    # Public method
    def check_result(self):
        if self.__grade >= 50:
            return "Pass"
        else:
            return "Fail"
        
    # String method
    def __str__(self):
        return f"Student Name: {self.__name}, Roll.No: {self.__roll_number}, Grade: {self.__grade}, Result: {self.check_result()}"
    


students = []
n = int(input("How many students: "))
for i in range(n):
    name = input("Enter student Name: ")
    roll = int(input("Enter roll number: "))
    grade = int(input("Enter grade (0-100): "))

    student = Student(name, roll, grade)
    students.append(student)

for s in students:
    print(s)

