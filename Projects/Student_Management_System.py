"""Project: Student Management System (Beginner OOP Project)
Concepts Covered: Classes, Objects, Encapsulation (getters/setters).

Project Description:
Build a simple program where you can:

Create a Student class with attributes: name, roll_no, marks.

Add methods to:

Display student details.

Update marks safely (encapsulation).

Create multiple student objects and manage them."""


class Student:

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.__marks = marks

    def add_marks(self, marks):
        self.__marks += marks
        print(f"Added {marks} marks. Total marks: {self.__marks}")

    # getter
    def get_marks(self):
        return self.__marks
    
    # setter
    def set_marks(self, new_marks):
        if new_marks >= 0:
            self.__marks = new_marks
            print(f"Marks Updates to: {self.__marks}")
        else:
            print("Invalid Marks! Cannot be Zero.")
    

    def display_info(self):
        print(f"Name: {self.name}, Roll_no: {self.roll_no}, Marks: {self.__marks}")


student1 = Student("Jahanzaib", 1034, 85)
student2 = Student("Hassan", 1121, 80)
student3 = Student("Waqas", 1010, 79)

student1.display_info()
student2.display_info()
student3.display_info()

print(student1.get_marks())
student1.set_marks(2000)
