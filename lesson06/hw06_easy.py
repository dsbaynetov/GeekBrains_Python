# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

#класс полигон
class Poligon:
    def __init__(self):
        pass

    # определение длинны фигуры
    def side_len(self, point1, point2):
        result = math.sqrt(abs(point1[0] - point2[0]) ** 2 + abs(point1[1] - point2[1]) ** 2)
        return result

class Triangle(Poligon):
    def __init__(self, point1, point2, point3):
        Poligon.__init__(self)
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    # определение длинны фигуры
    def side_len(self, point1, point2):
        result = math.sqrt(abs(point1[0] - point2[0]) ** 2 + abs(point1[1] - point2[1]) ** 2)
        return result

    def area(self):
        '''
        Площадь треугольника по формуле Герона
        :return:
        '''
        ab = Poligon.side_len(self, self.point1, self.point2)
        bc = Poligon.side_len(self, self.point2, self.point3)
        ca = Poligon.side_len(self, self.point1, self.point3)
        p = self.perimeter() / 2
        result = math.sqrt(p * (p - ab) * (p - bc) * (p - ca))
        return result

    def area_h(self):
        '''
        Площадь треугольника через высоту
        :return:
        '''
        #высота треугольника
        h =  self.height(self.point1, self.point3)

        #основание треугольника
        a = Poligon.side_len(self, self.point1, self.point3)

        #площадь
        result = a * h /2
        return result

        p = self.perimeter() / 2
        result = p * (p - ab) * (p - bc) * (p - ca)
        return result

    def height(self, point1, point2):
        '''
        определение высоты треугольника опущенной на сторону заданную гоординатами point1 и point2
        :return:
        '''

        #определеяем длины сторон
        ab = Poligon.side_len(self, self.point1, self.point2)
        bc = Poligon.side_len(self, self.point2, self.point3)
        ca = Poligon.side_len(self, self.point1, self.point3)

        #определяем полупериметр
        p = self.perimeter() / 2

        #длинна стороны на которую опускается высота
        side_h = Poligon.side_len(self, point1, point2)
        result = 2 * math.sqrt(p * (p - ab) * (p - bc) * (p - ca)) / side_h
        return result

    def perimeter(self):
        '''
        периметр треугольника
        :return:
        '''
        ab = Poligon.side_len(self, self.point1, self.point2)
        bc = Poligon.side_len(self, self.point2, self.point3)
        ca = Poligon.side_len(self, self.point1, self.point3)
        return (ab + bc + ca)

t1 = Triangle((2,1), (5,6), (5,1))
#print(t1.side_len([2,1], [5,6]))

print('\nЗадание-2.Easy')
print(f'Площадь треугольника по методу Герона: {t1.area()}')
print(f'Площадь треугольника через высоту: {t1.area_h()}')
print(f'Высота треугольника {t1.height(t1.point1, t1.point3)}')
print(f'Периметр треугольника {t1.perimeter()}')

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze(Poligon):
    def __init__(self, point1, point2, point3, point4):
        Poligon.__init__(self)
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4
        self.ab = Poligon.side_len(self, self.point1, self.point2)
        self.bc = Poligon.side_len(self, self.point2, self.point3)
        self.cd = Poligon.side_len(self, self.point3, self.point4)
        self.ad = Poligon.side_len(self, self.point1, self.point4)

    def is_trapeze(self):
        return (self.ab == self.cd)

    def side_len(self, point1, point2):
        return Poligon.side_len(point1, point2)

    def perimeter(self):
        return self.ab + self.bc + self.cd + self.ad

    def area(self):
        '''
        Площадь трапеции через стороны
        S = 	(a + b)/4 *	√4c2 - (a - b)2
        :return:
        '''
        return (self.ad + self.bc) / 4 * math.sqrt(4 * self.ab ** 2 - (self.ad - self.dc) ** 2)

#https://ru.onlinemschool.com/math/formula/trapezium_isosceles/#h0
t2 = Trapeze((10,1), (12,5), (16,5), (18,1))

print('\nЗадание-2.Easy')
print(f'Проверка, является ли фигура равнобедренной трапецией: {t2.is_trapeze()}')
print(f'Длины сторон ab: {t2.ab}, bc: {t2.bc}, cd: {t2.cd}, ad: {t2.ad}')
print(f'Периметр трапеции: {t2.perimeter()}')
print(f'Площадь трапеции: {t2.area()}')