# Create a class called Numbers, which has a single class attribute called  MULTIPLIER, and a constructor which takes the parameters x and y (these should all be numbers).
# i. Write a method called add which returnsthesumof the attributes x and y.
# ii. Write a class method called multiply, which takes a single number parameter a and returns the product of a and MULTIPLIER.
# iii. Write a static method called subtract, which takes two number parameters, b and c, and returns b -c.
# iv. Write a method called value which returns a tuple containing the values of x and y. Make this method into a property, and write a setter and a deleter for manipulating the values of x and y

class Numbers:
    MULTIPLIER = 10

    #constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self):
        return self.x + self.y
    
    def multiply(self, a):
        return self.MULTIPLIER * a
    
    #static method
    @staticmethod
    def subtract(b, c):
        return b - c

    #property method
    @property
    def value(self):
        return self.x, self.y

    #setters and deleters
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y

    def deleteX(self):
        del self.x
    def deleteY(self):
        del self.y

N = Numbers(20, 15)
print(N.add())
print(N.multiply(10))
print(N.subtract(63, 23))
N.setX(50)
N.setY(25)
print(N.value)
N.deleteX()
N.deleteY()