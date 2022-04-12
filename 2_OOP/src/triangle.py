from src.figure import BaseFigure
import math


class Triangle(BaseFigure):
    """ Класс с переменными и методами геометрической фигуры "треугольник" """

    def __init__(self, side_a, side_b, side_c):
        """ Метод-инициализатор класса "треугольник" """

        self.name = 'Triangle'
        self.angles = 3
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()

    def calculate_perimeter(self):
        """ Метод вычисляет периметр треугольника """

        perimeter = self.side_a + self.side_b + self.side_c
        return perimeter

    def calculate_area(self):
        """ Метод вычисляет площадь треугольника """

        half_perimeter = 0.5 * self.calculate_perimeter()
        area = math.sqrt(half_perimeter *
                         (half_perimeter - self.side_a) *
                         (half_perimeter - self.side_b) *
                         (half_perimeter - self.side_c))
        return area
