class Figure:
    unit = "cm"

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass

class Circle(Figure):
    pi = 3.14

    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return Circle.pi * (self.__radius**2)

    def info(self):
        print(f"CIRCLE:\n Radius: {self.__radius}\n Area: {self.calculate_area()}\n")

class Triangle(Figure):

    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return self.__side_b * self.__side_a / 2
    def info(self):
        print(f"TRIANGLE:\n Side(a): {self.__side_a}\n Side(b):{self.__side_b}\n Area:{self.calculate_area()}\n")

circle1 = Circle(2)
circle2 = Circle(6)

triangle1 = Triangle(3, 5)
triangle2 = Triangle(7, 4)
triangle3 = Triangle(9, 1)

tr = [triangle1, triangle2, triangle3]
cr = [circle1, circle2]

for i in tr:
    i.info()

for o in cr:
    o.info()

