# Multilevel Inheritance

class Employee:
    def __init__(self, empid, name):
        self.empid = empid
        self.name = name
    
    def printempinfo(self):
        print('Employee Id:', self.empid)
        print('Name:', self.name)

class Salary(Employee):
    def __init__(self, empid, name, salary):
        Employee.__init__(self, empid, name)
        self.salary = salary

    def printsalary(self):
        Employee.printempinfo(self)
        print('Salary:', self.salary)

class JobTitle(Salary):
    def __init__(self, empid, name, salary, title):
        Salary.__init__(self, empid, name, salary)
        self.title = title
    
    def printDetails(self):
        Salary.printsalary(self)
        print('Job Title:', self.title)

E = JobTitle(125, 'Jack Sparrow', 250000, 'Head of Department')
E.printDetails()