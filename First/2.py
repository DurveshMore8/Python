#Enter the number from the user and depending on whether te numbe is even or odd, print out an appropriate message to the user

number = int(input('Enter Number:'))

if number % 2 == 0 :
    print(str(number) + ' is an Even Number')
else:
    print(str(number) + ' is an Odd Number')