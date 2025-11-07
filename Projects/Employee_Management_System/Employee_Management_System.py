from abc import ABC, abstractmethod
import os

# Abstract Base Class
class Employee(ABC):

    # Constructor to initialize name, emp_id, department.
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department

    @abstractmethod
    def calculate_salary(self):
        pass
    
    # String method
    def __str__(self):
        return f"{self.__class__.__name__} | {self.name} - {self.emp_id} | Department: {self.department}"
        

# Full-Time Employee Class
class FullTimeEmployee(Employee):

    def __init__(self, name, emp_id, department, monthly_salary, bonus):
        super().__init__(name, emp_id, department)
        self.monthly_salary = monthly_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.monthly_salary + self.bonus
    
    def to_csv(self):
        return f"FullTimeEmployee,{self.name},{self.emp_id},{self.department},{self.monthly_salary},{self.bonus}"
    
# Part-Time Employee Class    
class PartTimeEmployee(Employee):

    def __init__(self, name, emp_id, department, hourly_rate, hours_worked):
        super().__init__(name, emp_id, department)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
    
    def to_csv(self):
        return f"PartTimeEmployee,{self.name},{self.emp_id},{self.department},{self.hourly_rate},{self.hours_worked}"


# Company Class    
class Company:
    
    # Constructor to store books
    def __init__(self):
        self.employees = []
        self.load_from_csv() # silently load existing data

    # Add employee in list of employee
    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} added successfully!")

    # Display employee info 
    def display_employees(self):
        if not self.employees:
            print("No Employees in Company")
        else:
            print("\n--- Employee List ---")
            for emp in self.employees:
                print(emp, "| Salary:", emp.calculate_salary())
    
    # Search employee by id
    def search_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                print("Employee Found:", emp)
                return emp
        print("Employee not found.")
        return None
    
    # Remove employee by id
    def remove_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                print(f"Employee '{emp_id}' removed successfully.")
                return
        print("Employee not found.")

    # Method to calculate total salary's
    def total_payroll(self):
        total = 0
        for emp in self.employees:
            total += emp.calculate_salary()
        return total
    
    # Save data to file
    def save_to_csv(self):
        with open("employee.csv", "w") as file:
                file.write("Type,Name,Emp_ID,Department,Salary/Rate,Bonus/Hours\n")
                for emp in self.employees:
                    file.write(emp.to_csv() + "\n")

    # Load data from file
    def load_from_csv(self):
        if not os.path.exists("employee.csv"):
            return  # silently skip if file doesn’t exist
        with open("employee.csv", "r") as file:
            next(file)  # skip header
            # Read the remaining lines
            for line in file:
                # Remove leading/trailing whitespace and split by comma
                parts = line.strip().split(",")
                # Assign parts to variables, ensuring there are enough elements
                if len(parts) < 6:
                    continue
                emp_type, name, emp_id, department, val1, val2 = parts

                emp_id = int(emp_id)
                val1 = float(val1)
                val2 = float(val2)

                if emp_type == "FullTimeEmployee":
                    employee = FullTimeEmployee(name, emp_id, department, val1, val2)
                elif emp_type == "PartTimeEmployee":
                    employee = PartTimeEmployee(name, emp_id, department, val1, val2)
                else:
                    continue
                self.employees.append(employee)

# Menu Function    
def menu():

    # Create company object
    company = Company()

    while True:
        print("\n===== Company Menu =====")
        print("1. Add Employee")
        print("2. Display Employee")
        print("3. Search Employee")
        print("4. Remove Employee")
        print("5. Total Payroll")
        print("6. Save & Exit")

        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Invalid input. Enter a number between 1-6.")
            continue
    
        # Add employee
        if choice == 1:
            name = input("Enter Employee Name: ")
            emp_id = int(input("Enter Employee ID: "))
            department = input("Enter Employee Department: ")
            emp_type = input("Enter type (F for Full-Time / P for Part-Time): ").lower()

            if emp_type == "f":
                monthly_salary = float(input("Enter Monthly Salary: "))
                bonus = float(input("Enter Bonus: "))
                employee = FullTimeEmployee(name, emp_id, department, monthly_salary, bonus)
            else:
                hourly_rate = float(input("Enter Hourly Rate: "))
                hours_worked = float(input("Enter Hours Worked: "))
                employee = PartTimeEmployee(name, emp_id, department, hourly_rate, hours_worked)

            company.add_employee(employee)

        # Display employee
        elif choice == 2:
            company.display_employees()

        # Search employee
        elif choice == 3:
            emp_id = int(input("Enter Employee ID  to Search: "))
            company.search_employee(emp_id)

        # Remove employee
        elif choice == 4:
            emp_id = int(input("Enter Employee ID to Remove: "))
            company.remove_employee(emp_id)

        # Calculate total_payroll
        elif choice == 5:
            print("Total Payroll:", company.total_payroll())

        # Save to file & Exit
        elif choice == 6:
            company.save_to_csv()
            print("Data Saved. GoodBye!")
            break

        else:
            print("Invalid choice. Try again.")

# Run Program            
if __name__ == "__main__":
    menu()
