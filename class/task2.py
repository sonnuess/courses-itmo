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

    def perimeter(self,a,b,c):
        length = a.distance(b) + b.distance(c) + c.distance(a)



    def area (self,a,b,c):
        p=self.perimeter(a,b,c)/2
        area = (p*(p-a)*(p-b)*(p-c))**0.5
    def __contains__(self,point):
        s1 = 
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
