from abc import abstractmethod


class EmployeeBase:
    @abstractmethod
    def add_employee(self, employee):
        pass

    @abstractmethod
    def remove_employee(self, employee):
        pass

    @abstractmethod
    def get_child(self, index):
        pass

    @abstractmethod
    def print(self):
        pass


class Developer(EmployeeBase):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def add_employee(self, employee):
        pass

    def remove_employee(self, employee):
        pass

    def get_child(self, index):
        return None

    def print(self):
        pass


class Manager(EmployeeBase):

    def __init__(self, name, salary, employees=None):
        if employees is None:
            self.employees = []
        self.name = name
        self.salary = salary

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def get_child(self, index):
        return self.employees[index]

    def print(self):
        print("----- Manager -----")
        print(f"Manager details - Name: {self.name}, Salary: {self.salary}\n")

        for emp in self.employees:
            emp.print()

