# Parent Class
class Student:

    # Constructor
    def __init__(self, name, roll_number, grade):
        self.__name = name
        self.__roll_number = roll_number
        self.grade = grade

    # Getter Method
    @property
    def grade(self):
        return self.__grade
    
    # Setter Method
    @grade.setter
    def grade(self, value):
        if 0 <= value <= 100:
            self.__grade = value
        else:
            self.__grade = 0
            print("Invalid grade. Must be between 0 and 100.")

    # Public Method
    def check_result(self):
        if self.__grade >= 50:
            return "Pass"
        else:
            return "Fail"
        
    # Str Method
    def __str__(self):
        return f"{self.__name}, {self.__roll_number}, {self.__grade}, {self.check_result()}"
    
# list to store student records
students = []
n = int(input("How many Students: "))
for i in range(n):
    name = input("Enter student Name: ")
    roll = int(input("Enter roll number: "))
    grade = int(input("Enter grade (0-100): "))

    student = Student(name, roll, grade)
    students.append(student)

# Write to a file
with open("students.csv", "w") as file:
    file.write("Name, Roll no, Grade, Result\n")
    for s in students:
        file.write(str(s) + "\n")
        
# Read from a file
with open("students.csv", "r") as file_content:
    content  = file_content.read()
    print(content)

# Search Student by Roll Number
roll_to_search = int(input("Enter roll number to search: "))

with open("students.csv", "r") as file:
    next(file) # Skip header
    found = False
    for line in file:
        data = line.strip().split(", ")
        if int(data[1]) == roll_to_search:
            print("Student Found", line.strip())
            found = True
            break
    
    if not found:
        print("Student not found.")

# Update Student Record by Roll Number
roll_to_update = int(input("Enter roll number to update: "))
updated = False

with open("students.csv", "r") as file:
    lines = file.readlines()

header = lines[0]   # Keep header safe
new_lines = [header]

for line in lines[1:]:   # Skip header
    data = line.strip().split(", ")
    if int(data[1]) == roll_to_update:
        new_grade = int(input(f"Enter new grade for {data[0]}: "))
        student = Student(data[0], int(data[1]), new_grade)  # Create updated student
        new_lines.append(str(student) + "\n")
        updated = True
    else:
        new_lines.append(line)

if updated:
    with open("students.csv", "w") as file:
        file.writelines(new_lines)
    print("Record updated successfully.")
else:
    print("Student not found.")

# Delete Student Record by Roll Number
roll_to_delete = int(input("Enter roll number to delete: "))
deleted = False

with open("students.csv", "r") as file:
    lines = file.readlines()

header = lines[0] # Keep header safe
new_lines = [header]

for line in lines[1:]:  # Skip header
    data = line.strip().split(", ")
    if int(data[1]) == roll_to_delete:
        print("Student Deleted: ", line.strip())
        deleted = True
    else:
        new_lines.append(line)

if deleted:
    with open("students.csv", "w") as file:
        file.writelines(new_lines)
        print("Record Deleted Successfully.")
else:
    print("Student not Found.")

