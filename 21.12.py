# class Bank:
#     def __init__(self, name, id, balance) -> None:
#         self.name = name 
#         self.id = id
#         self.balance = balance

#     def transaction(self, another_costumer, money):
#         if self.balance >= money:
#             self.balance = self.balance - money
#             another_costumer.balance = another_costumer.balance + money
        
#         else:
#             raise ValueError("Cartangizda yetarlicha pul mavjud emas")
        
# customer1 = Bank("Aziz", 1, 3000)
# customer2 = Bank("Farxod", 2, 14000)
# customer1.transaction(customer2, 4000)
# print(customer2.balance)
# print(customer1.balance)


# class Resturant:
#     def __init__(self) -> None:


#     def add_item(self, item, price, rating):
#         self.menu = [item, price, rating]
    
#     def remove_item(self, name):
#         for i in self.menu:
#             self.menu.remove(i)
    
#     def avarage_rating(self):
#         count = 0
#         av_r = 0
#         for i in self.menu[2]:
#             av_r += i
#             count += 1
#         av_r = av_r / count

#     def show_menu(self):
#         return self.menu

# r1 = Resturant("Pasta", 45000, 4.5)
# r1.add_item("Russian soup", 30000, 5)
# print(r1.show_menu())




class School:
    def __init__(self) -> None:
        people = dict()
        rooms = dict()
    def add_person(self, name, job):
        if job == "teacher":
            self.people["teacher"]  = {name}
        elif job == "student":
            self.people["student"] = {name}

    def remove(self, name):
        self.people.pop(name)

    def   create_class(self, room_number):
        self.rooms