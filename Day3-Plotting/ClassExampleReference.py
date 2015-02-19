"""
- This file contains a basis exampe of a class in python
- Classes are ways of storing data and functions that are related
- This class create a 2D vector object
"""
import math

class Vector2D:
    def __init__(self,xVal=0.0,yVal=0.0):
        self.x = xVal
        self.y = yVal
        
    def length(self):
        return math.sqrt((self.x**2 + self.y**2))
        
    def dot(self,other):
        return self.x*other.x + self.y*other.y
        
    def normalize(self):
        N = math.sqrt(self.dot(self))
        self.x = self.x/N
        self.y = self.y/N
        
A = Vector2D(2.0,3.0)
print A.x, A.y, A.length()
B = Vector2D(-3.0,-1.0)
print A.dot(B)
print B.dot(A)

print A.length()
A.normalize()
print A.length()