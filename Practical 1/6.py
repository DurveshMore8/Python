# Write a recursive function to print the factorial for a given number

def Factorial (no):
    if no == 0 or no == 1:
        return 1
    else:
        return (no * Factorial(no - 1))

number = int(input('Enter Number: '))
print('Factorial of', number, 'is', Factorial(number))