# Employee Management System

A small Python CLI demonstrating abstract base classes, inheritance, polymorphism, and CSV-based persistence for employee payroll.

## Concepts Covered
- Abstract Base Class (Employee) and abstract methods
- Inheritance: FullTimeEmployee and PartTimeEmployee
- Polymorphism: calculate_salary() implemented per subclass
- File I/O: load/save employees in CSV for persistent storage
- Simple CLI menu for CRUD-like operations

## Project Overview
This program models a Company that holds Employee objects. Full-time employees use monthly salary + bonus; part-time employees use hourly rate × hours worked. On start the app silently loads employee.csv (if present). Users can add, list, search, remove employees, view total payroll, and save data back to employee.csv.

## CSV Format (employee.csv)
Header:
Type,Name,Emp_ID,Department,Salary/Rate,Bonus/Hours

Example rows:
FullTimeEmployee,Jane Doe,101,Engineering,6000.0,500.0
PartTimeEmployee,Joe Bloggs,202,Support,25.0,120.0

## Quick Start
1. Save code to `company.py`.
2. (Optional) Create `employee.csv` with the header above.
3. Run:
python company.py
4. Use the menu (1–6). Choose "Save & Exit" to write `employee.csv`.

## Commands (menu)
1. Add Employee — choose F (full-time) or P (part-time) and enter details  
2. Display Employee — list all employees and computed salaries  
3. Search Employee — find by employee ID  
4. Remove Employee — delete by employee ID  
5. Total Payroll — sum of all salaries  
6. Save & Exit — write CSV and exit

## What you'll learn
- Designing with ABC and abstract methods
- Implementing polymorphic behavior for salary calculation
- Persisting objects as CSV and reconstructing them on load
- Building a minimal, user-driven CLI app
