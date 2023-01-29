# geometry file for 1.py

import math

def pointyShapeVolume(x, y, squareBase):
    if(squareBase == 'True'):
        return float((x * x) * (y / 3))
    elif(squareBase == 'False'):
        return float((math.pi * x * x) * (y / 3))
    else:
        print('Wrong Value of squareBase')

def circleArea(r):
    return float(math.pi * r * r)
def squareArea(s):
    return s * s