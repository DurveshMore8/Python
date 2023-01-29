#Write a program to implement exception handling.

class NegativeMarksError(Exception):
    pass
class OverValuedMarksError(Exception):
    pass
class FloatMarksError(Exception):
    pass

try:
    marks = int(input('Enter Marks: '))
    if marks < 0:
        raise NegativeMarksError
    if marks > 100:
        raise OverValuedMarksError
    if type(marks) == 'float':
        raise FloatMarksError
    
    if marks < 35:
        print('You are Fail!')
    else:
        print('You are Pass!')

except ValueError:
    print('Marks should be in Integar Form')
except NegativeMarksError:
    print('Marks cannot be Negative')
except OverValuedMarksError:
    print('Marks cannot be Greater than 100')

else:
    print('Code Runned Successful')

finally:
    print('Code Ended')