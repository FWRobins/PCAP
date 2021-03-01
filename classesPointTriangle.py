import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.sqrt(abs(self.__x-x)**2+abs(self.__y-y)**2)

    def distance_from_point(self, point):
        return math.sqrt(abs(self.__x-point._Point__x)**2+abs(self.__y-point._Point__y)**2)

# point1 = Point(0, 0)
# print(point1._Point__x, point1._Point__y)
# point2 = Point(1, 1)
# print(point2._Point__x, point2._Point__y)
# print(point1.distance_from_point(point2))
# print(point2.distance_from_xy(2, 0))

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__A = vertice1.distance_from_point(vertice2)
        self.__B = vertice1.distance_from_point(vertice3)
        self.__C = vertice3.distance_from_point(vertice2)

    def perimeter(self):
        return self.__A+self.__B+self.__C


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
