# Hybrid Inheritance

class Get:
    def GetValues(self):
        self.a = int(input('Enter 1st Number: '))
        self.b = int(input('Enter 2nd Number: '))

class Addition(Get):
    def Add(self):
        Get.GetValues(self)
        self.add = self.a + self.b

class Subtration(Get):
    def Subtract(self):
        Get.GetValues(self)
        self.sub = self.a - self.b

class Print(Addition, Subtration):
    def PrintAdd(self):
        Addition.Add(self)
        print('Addition is',self.add,'\n')
    
    def PrintSub(self):
        Subtration.Subtract(self)
        print('Subtraction is', self.sub)

O = Print()
O.PrintAdd()
O.PrintSub()