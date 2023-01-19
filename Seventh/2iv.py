# Hierarchical Inheritance

class GetParameters:
    def rec(self):
        self.l = int(input('Enter Length: '))
        self.b = int(input('Enter Breadth: '))
    
    def squ(self):
        self.s = int(input('\nEnter Side: '))

class Rectangle(GetParameters):
    def __init__(self):
        GetParameters.rec(self)
    
    def PrintPeri(self):
        self.peri = 2 * (self.l + self.b)
        print('Perimeter of Rectangle is', self.peri)

    def PrintArea(self):
        self.area = self.l * self.b
        print('Area of Rectangle is', self.area)

class Square(GetParameters):
    def __init__(self):
        GetParameters.squ(self)
    
    def PrintPeri(self):
        self.peri = 4 * self.s
        print('Perimeter of Square is', self.peri)
    
    def PrintArea(self):
        self.area = self.s * self.s
        print('Area of Square is', self.area)

R = Rectangle()
R.PrintPeri()
R.PrintArea()

S = Square()
S.PrintPeri()
S.PrintArea()