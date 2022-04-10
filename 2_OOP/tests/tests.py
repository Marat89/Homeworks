""" Тесты геометрических фигур"""

import pytest
from src.figure import BaseFigure
from src.triangle import Triangle
from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle

base_figure = BaseFigure()
triangle = Triangle(20, 20, 20)
rectangle = Rectangle(30, 30)
square = Square(40, 40)
circle = Circle(50)


class TestFigures:
    """ Тесты геометрических фигур"""

    def test_triangle_name(self):
        """ Тест на проверку имени треугольника"""
        assert base_figure.get_name(triangle) == 'Triangle'

    def test_rectangle_name(self):
        """ Проверка имени прямоугольника"""
        assert base_figure.get_name(rectangle) == 'Rectangle'

    def test_square_name(self):
        """ Проверка имени квадрата"""
        assert base_figure.get_name(square) == 'Square'

    def test_circle_name(self):
        """ Проверка имени круга"""
        assert base_figure.get_name(circle) == 'Circle'

    def test_triangle_area(self):
        """ Проверка вычисления площади треугольника"""
        assert round(triangle.calculate_area()) == 173

    def test_rectangle_area(self):
        """ Проверка вычисления площади прямоугольника"""
        assert rectangle.calculate_area() == 900

    def test_square_area(self):
        """ Проверка вычисления площади квадрата"""
        assert square.calculate_area() == 1600

    def test_circle_area(self):
        """ Проверка вычисления площади круга"""
        assert round(circle.calculate_area()) == 310063

    def test_triangle_perimeter(self):
        """ Проверка вычисления периметра треугольника"""
        assert triangle.calculate_perimeter() > triangle.side_a
        assert triangle.calculate_perimeter() > triangle.side_b
        assert triangle.calculate_perimeter() > triangle.side_c

    def test_rectangle_perimeter(self):
        """ Проверка вычисления периметра прямогольника"""
        assert rectangle.calculate_perimeter() > rectangle.side_a
        assert rectangle.calculate_perimeter() > rectangle.side_b

    def test_square_perimeter(self):
        """ Проверка вычисления периметра квадрата"""
        assert square.calculate_perimeter() > square.side_a
        assert square.calculate_perimeter() > square.side_b

    def test_circle_perimeter(self):
        """ Проверка вычисления периметра круга"""
        assert circle.calculate_perimeter() > circle.radius

    @pytest.mark.parametrize('other_figure', [rectangle, triangle, square, circle, 'abrakadabra', 123456])
    @pytest.mark.parametrize('default_figure', [triangle, rectangle, square, circle])
    def test_add_square(self, other_figure, default_figure):
        """ Проверка метода сложения площадей фигур"""
        if isinstance(other_figure, BaseFigure):
            assert default_figure.add_square(other_figure) == default_figure.area + other_figure.area
        else:
            assert default_figure.add_square(other_figure) == 'Передан неверный класс геометрической фигуры'
