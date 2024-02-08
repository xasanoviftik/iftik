from abc import ABC, abstractmethod 
import math
"""
1-mashq
"""

# class Z:
#     pass

# class K1(Z):
#     pass

# class K2(Z):
#     pass

# class K3(Z):
#     pass

# class C(K1):
#     pass

# class A(K1, K3):
#     pass

# class B(K1, K2):
#     pass

# class D(K3, K2):
#     pass

# class E(K2):
#     pass

# class O(A, B, C, D, E):
#     pass

# print(O.mro())


"""
2
"""
# class O:
#     pass

# class D(O):
#     pass

# class E(O):
#     pass

# class F(O):
#     pass

# class B(D, E):
#     pass

# class C(D, F):
#     pass

# class A(B, C):
#     pass

# print(A.mro())


"""
3
"""


# class A:
#     pass

# class D(A):
#     pass

# class B(A):
#     pass

# class C(B):
#     pass

# class E(C, D, A):
#     pass

# class B(A):
#     pass

# class F(D):
#     pass

# class G(E, C):
#     pass

# class H(E, B):
#     pass

# class O(F, G, H):
#     pass

# print(O.mro())


"""
4
"""
# class D:
#     pass

# class C(D):
#     pass 

# class B(C, D):
#     pass

# class A(C):
#     pass


# print(A.mro())
# print(B.mro())



"""
2-mashq
# """

# def tangalar(tanga, qiymat):
#     tangalar = sorted(tanga, reverse=True)
#     natija = []
#     for i in tangalar:
#         while qiymat >= i:
#             qiymat -= i
#             natija.append(i)
#     return natija

# tanga = [1, 5, 10, 25, 100]
# qiymat = 15 
# print(tangalar(tanga, qiymat))


"""
3-mashq
"""

# class Shape:
#     def __init__(self, color, filled) -> None:
#         self.color = color
#         self.filled = filled

#     def getColor(self):
#         return self.color
    
#     def setColor(self, color):
#         self.color =color

#     def isFilled(self):
#         return self.filled
    
#     def setFilled(self, filled):
#         self.filled = filled

    
#     @abstractmethod
#     def getArea(self):
#         pass

#     @abstractmethod
#     def getPerimeter(self):
#         pass

#     @abstractmethod
#     def toString(self):
#         pass

# class Circle(Shape):
#     def __init__(self, color, filled, radius) -> None:
#         super().__init__(color, filled)
#         self.radius = radius

#     def getRadius(self):
#         return self.radius
    
#     def setRadius(self, radius):
#         self.radius = radius

#     def getArea(self):
#         return self.radius * math.pi ** 2 
    
#     def getPerimeter(self):
#         return self.radius * math.pi * 2

#     def toString(self):
#         return f"Shape{self.color}, {self.filled}, {self.radius}"

# class Rectangle(Shape):
#     def __init__(self, color, filled, width, length) -> None:
#         super().__init__(color, filled)
#         self.width = width
#         self.length = length

#     def getWidth(self):
#         return self.width
    
#     def setWidth(self, width):
#         self.width = width
    
#     def getLength(self):
#         return self.length
    
#     def setWidth(self, length):
#         self.length = length

#     def getArea(self):
#         return self.width * self.length
    
#     def getPerimeter(self):
#         return (self.length + self.width) * 2

#     def toString(self):
#         return f"REctangle[Shape{self.color}, {self.filled}], {self.width}, {self.length}"
    
