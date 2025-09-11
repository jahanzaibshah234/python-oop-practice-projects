#User function Template for python3
# Implement Student, Faculty and PhdStudent classes here
class Student:
    
    def __init__(self, sid, deptid):
        self.sid = sid
        self.deptid = deptid
        
    def get_info(self):
        return f"StudentID:{self.sid} DepartmentID:{deptid}"
        
        
class Faculty:
    
    def __init__(self, eid, deptid):
        self.eid = eid
        self.deptid = deptid
        
    def get_info(self):
        return f"EmployeeID:{eid} DepartmentID:{deptid}"
        
class PhDStudent(Student, Faculty):
    def __init__(self, sid, eid, deptid):
        super().__init__(sid, deptid)
        super().__init__(eid, deptid)
        
    def get_info(self):
        return f"StudentID:{sid} EmployeeID:{eid} DepartmentID:{deptid}"