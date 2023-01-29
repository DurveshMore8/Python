# Write a function that reverses the user defined value

def reverseno(no):
    reverse = 0
    while no > 0 :
        digit = no % 10
        no = no // 10
        reverse = (reverse * 10) + digit
    return reverse

number = int(input('Enter Number:'))

print('Reverse of', number, 'is', reverseno(number))