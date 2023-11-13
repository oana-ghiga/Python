#Create a class hierarchy for shapes, starting with a base class Shape. Then, create subclasses like Circle, Rectangle, and Triangle. Implement methods to calculate area and perimeter for each shape.

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, name, a, b, c):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c


circle = Circle("Circle", 5)
print("Arie cerc:",circle.area())
print("Perimetru cerc:",circle.perimeter())

rectangle = Rectangle("Rectangle", 5, 10)
print("Arie dreptunghi",rectangle.area())
print("Perimentru dreptunghi",rectangle.perimeter())

triangle = Triangle("Triangle", 3, 4, 5)
print("Arie triunghi",triangle.area())
print("Perimentru triunghi",triangle.perimeter())