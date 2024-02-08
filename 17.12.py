"""
1-misol
"""
# def check_none(func):

#     def wrapper(value):
#         if value is not None:
#             func(value)
        
#         else:
#             pass
#     return wrapper

# @check_none
# def printer(value): 
#     print(value)


# printer("Salom")
# printer(42)
# printer(None)
# printer([1, 2, 3])

"""
2,3-misol
"""

# class Tortburchak:
#     def __init__(self, uzunlik, kenglik, rang):
#         self.uzunlik = uzunlik
#         self.kenglik = kenglik
#         self.rang = rang
#         self.read_only = False

#     @property
#     def yuza(self):
#         return self.uzunlik * self.kenglik

#     @property
#     def color(self):
#         return self.rang

#     @color.setter
#     def color(self, new_color):
#         if not self.read_only:
#             self.rang = new_color
#         else:
#             raise AttributeError("Rang xususiyati o'zgartirib bo'lmaydi")

# t = Tortburchak(10, 5, "qizil")

# print("To'rtburchakning yuzasi:", t.yuza)
# print("To'rtburchakning rangi:", t.color)

# t.color = "yashil"
# print("To'rtburchakning yangi rangi:", t.color)

# t.read_only = True

# t.color = "ko'k"
# print("To'rtburchakning yangi rangi:", t.color)

"""
4-mashq
"""

class Circle:
    def __init__(self, radius) -> None:
        self._radius = radius

    @property
    def radius(self):
        return self.radius
    @radius.setter
    def radius(self, new_r):
        self._radius = new_r

    @radius.getter
    def radius(self):
        raise AttributeError("Radius xususiyati faqat o'zgartirish uchun mo'ljallangan")
c = Circle(5)
c.radius = 10
print(c.radius)