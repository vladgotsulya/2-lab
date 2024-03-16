import math

class GeometricFigure:
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Ellipse(GeometricFigure):
    def __init__(self, semi_major_axis, semi_minor_axis):
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis

    def calculate_area(self):
        return math.pi * self.semi_major_axis * self.semi_minor_axis

    def calculate_perimeter(self):
        return 2 * math.pi * math.sqrt((self.semi_major_axis ** 2 + self.semi_minor_axis ** 2) / 2)

class Square(GeometricFigure):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

    def calculate_perimeter(self):
        return 4 * self.side_length

class Trapezoid(GeometricFigure):
    def __init__(self, base1, base2, height, side1, side2):
        self.base1 = base1
        self.base2 = base2
        self.height = height
        self.side1 = side1
        self.side2 = side2

    def calculate_area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def calculate_perimeter(self):
        return self.base1 + self.base2 + self.side1 + self.side2


choice = input("Выберите тип фигуры (1 - эллипс, 2 - квадрат, 3 - трапеция): ")

if choice == "1":
    semi_major_axis = float(input("Введите большую полуось эллипса: "))
    semi_minor_axis = float(input("Введите малую полуось эллипса: "))
    ellipse = Ellipse(semi_major_axis, semi_minor_axis)
    print("Площадь эллипса:", ellipse.calculate_area())
    print("Периметр эллипса:", ellipse.calculate_perimeter())

elif choice == "2":
    side_length = float(input("Введите длину стороны квадрата: "))
    square = Square(side_length)
    print("Площадь квадрата:", square.calculate_area())
    print("Периметр квадрата:", square.calculate_perimeter())

elif choice == "3":
    base1 = float(input("Введите длину нижнего основания трапеции: "))
    base2 = float(input("Введите длину верхнего основания трапеции: "))
    height = float(input("Введите высоту трапеции: "))
    side1 = float(input("Введите длину боковой стороны трапеции: "))
    side2 = float(input("Введите длину другой боковой стороны трапеции: "))
    trapezoid = Trapezoid(base1, base2, height, side1, side2)
    print("Площадь трапеции:", trapezoid.calculate_area())
    print("Периметр трапеции:", trapezoid.calculate_perimeter())

else:
    print("Некорректный выбор.")