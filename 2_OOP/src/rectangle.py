from src.figure import BaseFigure


class Rectangle(BaseFigure):
    """ Класс с переменными и методами геометрической фигуры "прямоугольник" """

    def __init__(self, side_a, side_b):
        """ Метод-инициализатор класса "прямоугольник" """

        self.name = 'Rectangle'
        self.angles = 4
        self.side_a = side_a
        self.side_b = side_b
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()

    def calculate_perimeter(self):
        """ Метод вычисляет периметр прямоугольника """

        perimeter = 2 * (self.side_a + self.side_b)
        return perimeter

    def calculate_area(self):
        """ Метод вычисляет площадь прямоугольника """

        area = self.side_a * self.side_b
        return area
