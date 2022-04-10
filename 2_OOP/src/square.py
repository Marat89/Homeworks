from src.figure import BaseFigure


class Square(BaseFigure):
    """ Класс с переменными и методами геометрической фигуры "квадрат" """

    def __init__(self, side_a, side_b):
        """ Метод-инициализатор класса "квадрат" """

        self.name = 'Square'
        self.angles = 4
        self.side_a = side_a
        self.side_b = side_b
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()

    def calculate_perimeter(self):
        """ Метод вычисляет периметр квадрата """

        perimeter = 2 * (self.side_a + self.side_b)
        return perimeter

    def calculate_area(self):
        """ Метод вычисляет площадь квадрата """

        area = self.side_a * self.side_b
        return area
