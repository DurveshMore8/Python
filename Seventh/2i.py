# Implement the concept of inheritance using python.
# Single Inheritance

class GetNumber:
    def __init__(self):
        self.number = int(input('Enter the Number:'))

class PrintTable(GetNumber):
    def printt(self):
        print('Table of', self.number, 'till 10 is')
        for i in range(1,11):
            print(self.number, '*', i, '=', self.number * i)

N = PrintTable()
N.printt()