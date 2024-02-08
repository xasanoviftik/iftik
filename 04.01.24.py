import math
from abc import ABC, abstractmethod 
class Shakl:
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def yuza(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Uchburchak(Shakl):
    def __init__(self, a , b,  c, h) -> None:
        self.a = a
        self.b = b
        self.h = h
        self.c = c

    def yuza(self):
        return 1/2 * self.b * self.h

    def perimeter(self):
        return self.a + self.b + self.c


class Doira(Shakl):
    def __init__(self, r) -> None:
        self.r = r

    def yuza(self):
        return self.r **2 * math.pi

    def perimeter(self):
        return self.r * 2 * math.pi

    