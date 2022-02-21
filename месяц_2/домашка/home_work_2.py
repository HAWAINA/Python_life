class Figure:
    unit = "cm"

    def __init__(self):
        self.__calculate_perimeter()
        self.calculate_area()

    def get_perimeter(self):
        return self.__perimeter

    def set_perimeter(self, perimeter):
        self.__perimeter = perimeter

    def __str__(self) -> None:
        pass

    def calculate_area(self):
        print("Calculate Area")

    def __calculate_perimeter(self):
        print("Calculate Perimeter")

    def info(self):
        pass

class Square(Figure):

    def __init__(self, __side_length):
        self.__side_length = __side_length
        self.calculate_area()
        self.perimeter = self.__calculate_perimeter()

    def calculate_area(self):
        return f"Square: {self.__side_length * 2}"

    def __calculate_perimeter(self):
        return f"Perimeter: {self.__side_length * 4}"

    def info(self):
        print(f"SQUARE:\n Side length:{self.__side_length}\n Area:{self.calculate_area()}\n {self.__calculate_perimeter()}\n")

class Rectangle(Figure):

    def __init__(self, __length, __width):
        self.__width = __width
        self.__length = __length

    def calculate_area(self):
        return self.__length * self.__width

    def __calculate_perimeter(self):
        return (self.__length + self.__width) * 2

    def info(self):
        print(
            f"RECTANGLE:\n Length:{self.__length}cm\n Width:{self.__width}cm\n Perimeter:{self.__calculate_perimeter()}cm\n Area:{self.calculate_area()}cm \n")

s1 = Square(1)
s2 = Square(3)

r1 = Rectangle(5, 8)
r2 = Rectangle(1, 3)
r3 = Rectangle(1, 4)

rec = [r1, r2, r3]
sq = [s1, s2]
for i in rec:
    i.info()

for j in sq:
    j.info()
