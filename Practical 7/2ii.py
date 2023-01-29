# Multiple Inheritance

class getPerimeter:
    def __init__(self):
        self.a = int(input('Enter First Side: '))
        self.b = int(input('Enter Second Side: '))
        self.c = int(input('Enter Third Side: '))
    
class getArea:
    def __init__(self):
        self.b = int(input('Enter Base: '))
        self.h = int(input('Enter Height: '))

class printValues(getPerimeter, getArea):
    def perimeter(self):
        self.perimeter = self.a + self.b + self.c
        print('Perimeter of Triangle is',self.perimeter)
        print()
    
    def area(self):
        getArea.__init__(self)
        self.area = (0.5) * self.b * self.h
        print('Area of Triangle is',self.area)

Triangle = printValues()
Triangle.perimeter()
Triangle.area()