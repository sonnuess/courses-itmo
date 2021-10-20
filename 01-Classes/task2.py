class Point:
    x: float
    y: float
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __copy__(self):
        return self.__copy__()

    def distance(self,other):
        import math
        dist = math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
        return dist

class Triangle:
    a: Point
    b: Point
    c: Point
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        length = 0
        



    def area (self):
        # использовать периметр и найти площадь через формулу герона
    def __contains__(self,point):
        # модуль , который вызовет магический метод __contains__
        # сложить площади треугольников, если их сумма равна площади большого треугольника, то точка находится внутри треугольника
        # если точка находится на стороне треуг-ка, то площадь 1 из них = 0, площадь других = площади большого треуг-ка


class Circle:
    center: Point
    radius: float
    def __init__(self,center,radius):
    def perimeter(self):
    def area(self):
    def __contains__(self, point):
    def intersects(self,other):
