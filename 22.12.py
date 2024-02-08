import random
from abc import ABC, abstractmethod
"""
1-mashq
"""

# class RatsionRaqam:
#     def __init__(self, a, b) -> None:
#         self.a = a
#         self.b = b

#     def __str__(self) -> str:
#         return f"{self.a}-birinchi son \n{self.b}-ikkinchi son"

#     def __add__(self):
#         return self.a + self.b
    
#     def __sub__(self):
#         return self.a - self.b

#     def __mul__(self):
#         return self.a * self.b
    
#     def __div__(self):
#         return self.a / self.b
    
# calculation = RatsionRaqam(12, 2)

# print(calculation.__add__())
# print(calculation.__sub__())
# print(calculation.__mul__())
# print(calculation.__div__())
# print(calculation)


"""
2-mashq
"""

# class MusicLibrary:
#     def __init__(self) -> None:
#         self.listofmusic = list()

#     def add(self, music):
#         self.listofmusic += [music]
    
#     def delete(self, music):
#         self.listofmusic.remove(music)


#     def random_music(self):
#         return random.choice(self.listofmusic)
    
#     def show_list(self):
#         return self.listofmusic
    
# m1 = MusicLibrary()
# m1.add("Bones")
# m1.add("Demons")
# m1.add("Without me")
# m1.add("Mockinbird")
# m1.delete("Mockinbird")
# print(m1.random_music())
# print(m1.show_list())

"""
3-mashq
"""

# class Animal(ABC):

#     @abstractmethod   
#     def uxlash():
#         pass

#     @abstractmethod
#     def yeyish():
#         pass

# class Kuchuk(Animal):
    
#     def uxlash(self):
#         return "kuchuk uhlamoqda"
    
#     def yeyish(self):
#         return "kuchuk yemoqda"
    
# k1 = Kuchuk()
# print(k1.yeyish())

# class Mushuk(Animal):
    
#     def uxlash(self):
#         return "mushuk uhlamoqda"
    
#     def yeyish(self):
#         return "mushuk yemoqda"
    
# m1 = Mushuk
# print(m1.yeyish())



"""
4-mashq
"""

class Doira:
    pi = 3,14
    def __init__(self, radius) -> None:
        self.__radius = radius

        def yuza(self):
            return Doira.pi * self.__radius
        
d = Doira(5)
print(d.yuza()) 
print(d.__radius)
        

