# Design a class that store the information of student and display the same

class student:
    def __init__(self):
        self.name = input('Enter Name: ')
        self.classs = input('Enter Class: ')
        self.course = input('Enter Course: ')
        self.rollno = input('Enter Roll No: ')
        self.age = int(input('Enter Age: '))
        print()
    
    def show(self):
        print('Name: ', self.name)
        print('Class: ', self.classs)
        print('Course: ', self.course)
        print('Roll No: ',self.rollno)
        print('Age: ', self.age)
        print()

student1 = student()
student1.show()

student2 = student()
student2.show()