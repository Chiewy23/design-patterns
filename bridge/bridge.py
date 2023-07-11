from abc import abstractmethod


# ----- BASE TYPES -----

class EmployeeBase:
    @abstractmethod
    def employee_type(self):
        pass


class DepartmentBase:
    def __init__(self, employee):
        self.employee = employee

    @abstractmethod
    def assign_employee(self):
        pass


# ----- SUB TYPES -----
class SalesDepartment(DepartmentBase):
    def __init__(self, employee):
        super().__init__(employee)

    def assign_employee(self):
        self.employee.employee_type()


class ITDepartment(DepartmentBase):
    def __init__(self, employee):
        super().__init__(employee)

    def assign_employee(self):
        self.employee.employee_type()


class PartTimeEmployee(EmployeeBase):
    def employee_type(self):
        print("Part-time employee")


class FullTimeEmployee(EmployeeBase):
    def employee_type(self):
        print("Full-time employee")
