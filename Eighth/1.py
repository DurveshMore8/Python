import geometry

print(dir(geometry))

dim = int(input('Enter Side/Radius: '))
height = int(input('Enter Height: '))
value = input('Enter Operation: ')

ans = geometry.pointyShapeVolume(dim, height, value)
if(value == 'True'):
    print('Volume of Square Pyramid is', ans)
    area = geometry.squareArea(dim)
    print('Area of Square is', area)
elif (value == 'False'):
    print('Volume of Right Circular Cone is', ans)
    area = geometry.circleArea(dim)
    print('Area of Circle is', area)