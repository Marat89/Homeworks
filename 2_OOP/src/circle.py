from src.figure import BaseFigure
from math import pi


class Circle(BaseFigure):
    """ Класс с переменными и методами геометрической фигуры "круг" """

    def __init__(self, radius):
        """ Метод-инициализатор класса "круг" """

        self.name = 'Circle'
        self.angles = 0
        self.radius = radius
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()

    def calculate_perimeter(self):
        """ Метод вычисляет периметр круга """

        perimeter = 2 * pi * self.radius
        return perimeter

    def calculate_area(self):
        """ Метод вычисляет площадь круга """

        area = pi * (self.perimeter ** 2)
        print(area)
        return area
