# Write a function to check the input value is Armstrong and also write the function for Palindrome

def Armstrong(no):
    temp = no
    product = 0
    while temp>0:
        digit = temp % 10
        temp = temp // 10
        product = product + (digit * digit * digit)
    if no == product:
        return True
    else:
        return False

def Palindrome(no):
    temp = no
    rev = 0
    while temp > 0:
        digit = temp % 10
        temp = temp // 10
        rev = (rev * 10) + digit
    
    if no == rev:
        return True
    else:
        return False

value = int(input('Enter number for Armstrong: '))
if Armstrong(value):
    print(value,'is an Armstrong')
else:
    print(value,'is not an Armstrong')

value = int(input('\nEnter number for Palindrome: '))
if Palindrome(value):
    print(value,'is a Palindrome')
else:
    print(value,'is not a Palindrome')