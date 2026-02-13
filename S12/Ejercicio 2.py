from abc import ABC, abstractclassmethod
import math

class Shape(ABC):
    perimeter = 0
    area = 0


    @abstractclassmethod
    def calculate_perimeter():
        pass
    @abstractclassmethod
    def calculate_area():
        pass

class Circle(Shape):
    
    def __init__(self,radius):
        self.radius = radius
    
    def calculate_perimeter(self):
        self.perimeter = 2 * math.pi * self.radius
        print(f"El perimetro del circulo es : {self.perimeter}")

    def calculate_area(self):
        self.area = math.pi * self.radius**2
        print(f"El area del circulo es : {self.area}")

        

class Square(Shape):
    
    def __init__(self,side):
        self.side = side

    def calculate_perimeter(self):
        self.perimeter = self.side * 4
        print(f"El perimetro del cuadrado es : {self.perimeter}")

    def calculate_area(self):
        self.area = self.side * self.side
        print(f"El area del cuadrado es : {self.area}")


class Rectangle(Shape):

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        self.perimeter = 2 * (self.width + self.height)
        print(f"El perimetro del rectangulo es : {self.perimeter}")


    def calculate_area(self):
        self.area = self.height*self.width
        print(f"El area del rectangulo es : {self.area}")

Circle_1 = Circle(8)
Square_1 = Square(5)
Rectangle_1 = Rectangle(20,20)


Circle_1.calculate_area()
Circle_1.calculate_perimeter()

Square_1.calculate_perimeter()
Square_1.calculate_area()

Rectangle_1.calculate_perimeter()
Rectangle_1.calculate_area()



