# class Bird:
    
#     def fly(self):
#         return "Ko'p qushlar ucha olishadi, lekin bazilari ucha olishmaydi!"

# class Burgut(Bird):

#     def fly(self):
#         return "Ucha oladi"
    
# class Pingvin(Bird):

#     def fly(self):
#         return "Ucha olmaydi"
    
# p1 = Pingvin()
# print(p1.fly())
# b1 = Burgut()
# print(b1.fly())



# class ShoppingCard:
#     def __init__(self) -> None:
#         self.items = dict()
#     def add_item(self, name, price):
#         self.items[name] = price

#     def remove_item(self, name):
#         if name in self.items.keys():
#             del self.items[name]
    
#     def total_price(self):
#         return sum(self.items.values())
# sh1 = ShoppingCard()
# sh1.add_item("ruchka", 1500)
# sh1.add_item("rezinka", 5000)
# sh1.add_item("olma", 9000)
# sh1.remove_item("rezinka")
# print(sh1.total_price())


import itertools

class Pairs:
    def __init__(self, numbers, target) -> None:
        self.numbers = numbers
        self.target  = target 
        self.summa = int()
    def find(self):
        result = itertools.combinations(self.numbers, 2)
        for i in result:
            print(i)
            for j in i:
                self.summa += j
                print(self.summa)
                if self.summa == self.target:
                    return i
p1 = Pairs([10, 20, 30, 40, 50, 60, 70], 50)
print(p1.find())