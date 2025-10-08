class Circle:
    def __init__(self,radius):
        self.radius = radius

    def get_area (self):

        self.area = 3.14 * self.radius ** 2
        print(f"El area del circulo es de {self.area}")
    

first_circle = Circle(3)
second_circle = Circle(7)
third_circle = Circle(10)

first_circle.get_area()
second_circle.get_area()
third_circle.get_area()
    

