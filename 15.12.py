"""
1-mashq
"""


class Transport:
    def __init__(self, max_tezlik, yurgan_masofa,) -> None:
        self.max_tezlik = max_tezlik 
        self.yurgan_masofa = yurgan_masofa

t1 = Transport(140, "200000 km")

"""
2-mashq
"""

class Reverse:
    def __init__(self, text: str) -> None:
        self.text = text
    
    def reverse(self):
        return self.text[::-1]
    
r1 = Reverse("Farhod va Shirin")
print(r1.reverse())

class Square:
    def __init__(self, a) -> None:
        self.a =  a

    def perimetr(self):
        return self.a * 4
    
    def area(self):
        return self.a ** 2
    
s1 =  Square(3)
print(s1.perimetr())

