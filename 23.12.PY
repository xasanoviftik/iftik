class Department:
    def __init__(self, deparmet_name, employee) -> None:
        self.deparmet_name = deparmet_name
        self.employee = employee
    
    def add_employee(self, name, job, salary):
        self.employee[name] = {job: salary}

    def show_employee(self, name):
        return self.employee[name]
    
class Employee:
    def __init__(self, name, job, salary) -> None:
        self.name = name
        self.job =job 
        self.salary = salary
        self.employee = dict()
    
    def employee(self):
        self.employee[self.name] = {self.job: self.salary}

w1 = Employee("Aziz", "waiter", 120)
d1 = Department("MacDonalds", w1.employee)
d1.add_employee("Kamal", "driver", 130)
d1.add_employee
print(d1.show_employee("Aziz"))