#User function Template for python3
# Implement Employee and SalesEmployee classes here
class Employee:
    
    def __init__(self, id, salary):
        self.id = id
        self.salary = salary
        
    
class SalesEmployee(Employee):
    def __init__(self, id, salary, sales):
        super().__init__(id, salary)
        self.sales = sales
        


