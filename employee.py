class Department:
    """
        department_name
        add_employee()
        show_employees()
    """
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
        else:
            raise ValueError("Employee must be a type of Employee class")

    def show_employees(self):
        print("Name\tJob\tSalary")
        for emp in self.employees:
            print(f"{emp.name}\t{emp.job}\t{emp.salary}")


class Employee:
    """
        name
        job
        salary
    """
    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.salary = salary


emp1 = Employee("John", "Software Engineer", 50000)
emp2 = Employee("Tom", "Recruiter", 60000)
emp3 = Employee("Anna", "Sales Representative", 55000)


sales = Department("Sales")
sales.add_employee(emp1)
sales.add_employee(emp2)
sales.add_employee(emp3)

sales.show_employees()
