import math
# class Person:
#     def __init__(self, name, address) -> None:
#         self.name= name 
#         self.address = address

#     def getName(self):
#         return self.name
    
#     def getAddress(self):
#         return self.address
    
#     def setAddress(self, address:str):
#         self.address= address

#     def toString(self):
#         return f"Person {self.name} {self.address}"


# class Student(Person):
#     def __init__(self, name, address, program, year, fee) -> None:
#         super().__init__(name, address)
#         self.program = program
#         self.year = year
#         self.fee = fee


#     def getProgram(self):
#         return self.program
    
#     def setProgram(self, program):
#         self.program = program

#     def getYear(self):
#         return self.year
    
#     def setYear(self, year):
#         self.year = year


#     def getFee(self):
#         return self.fee
    
#     def setFee(self, fee):
#         self.fee = fee

#     def toString(self):
#         return f"Student{super().toString()}, {self.program}, {self.year}, {self.fee}"
    
# class Staff(Person):
#     def __init__(self, name, address, school, pay) -> None:
#         super().__init__(name, address)
#         self.school = school
#         self.pay = pay

#     def getSchool(self):
#         return self.school
    
#     def setSchool(self, school):
#         self.school = school

#     def getPay(self):
#         return self.pay
    
#     def setPay(self, pay):
#         self.pay = pay

#     def toString(self):
#         return f"{super().toString()}, {self.school}, {self.pay}"
    
# s1 = Staff("Aziz", "Amir Temur 30uy", "16-maktab", 2000)
# s1.setSchool("15-maktab")
# s1.setAddress("Kichik Nohiya 45uy")
# print(s1.toString())

# student1 = Student("Farhod", "Alsher Navoiy 67-uy", "data science", 3, 3000)
# print(student1.getFee())
# student1.setYear(1)
# print(student1.toString())

class Circle:

    def __init__(self, radius) -> None:
        self.radius = radius
    
    def area(self):
        return self.radius * 2 * math.pi
circle1 = Circle(3)
class Cylinder:
    def __init__(self, circle:Circle, height) -> None:
        self.height = height
        self.circle = circle

    def volume(self):
        return self.circle.area() * self.height
    
cylinder1 = Cylinder(3, 12)
print(cylinder1.volume())
