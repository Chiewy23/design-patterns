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

    @abstractmethod
    def get_employee_count(self):
        pass


# ----- SUB TYPES -----
class SalesDepartment(DepartmentBase):
    def __init__(self, employee):
        super().__init__(employee)
        self.department_employees = []

    def assign_employee(self):
        print("Sales department assigned")
        self.employee.employee_type()
        self.department_employees.append(self.employee)

    def get_employee_count(self):
        return len(self.department_employees)


class ITDepartment(DepartmentBase):
    def __init__(self, employee):
        super().__init__(employee)
        self.department_employees = []

    def assign_employee(self):
        print("IT department assigned")
        self.employee.employee_type()
        self.department_employees.append(self.employee)

    def get_employee_count(self):
        return len(self.department_employees)


class PartTimeEmployee(EmployeeBase):
    def employee_type(self):
        print("Part-time employee")


class FullTimeEmployee(EmployeeBase):
    def employee_type(self):
        print("Full-time employee")
