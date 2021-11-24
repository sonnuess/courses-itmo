# задача 1
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def dist(self,other):
        if isinstance(other, Point):
            return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2)**0.5

class Vector(Point):
    def length(self, other):
        if isinstance(other, Vector):
            return self.dist(other.x, other.y)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(Point(self.x + other.x, self.y + other.y))

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(Point(self.x - other.x, self.y - other.y))


    def __str__(self):
        return f'Vector<x={self.x}, y={self.y}>'

    def __mul__(self, other):
        if isinstance(other,(int,float)):
            return Vector(Point(self.x * other.x, self.y * other.y))
        elif isinstance(other, self):
            return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return self * other

# задача 2

class Vehicle:
    def __init__(self,position):        #
        if isinstance(position, Point):
            self.position = position
        self.vector =  Vector(Point(self._position))  #???
        self._path = [] # list include all points
        self.is_recording: False # exists recording or not
                            #    direction: Vector
                            #   _position: Point
                            #  _path: []

    @property       # make privacy
    def _position(self):
        return self._position

    @property       # make privacy
    def _path(self):
        return self._path

    def __init__(self,position):
        self.is_recording = True
        self._path = []
        position = (self.x,self.y)
        self.

    def move(self,n):
        self.# дописать



class Car(Vehicle):
    def __init__(self, position, gas, gas_per_unit):
        self.__gas = 1 #
        self.__gas_per_unit = 1 #

    @property.setter # read setters / getters in matireals
    def gas(self):
        return self.__gas

    @property.setter
    def __gas_per_unit(self):
        return self.__gas_per_unit


    def (self, value):
        pass
    def (self):
        return

    @property.setter
    def (self, value):
        pass
