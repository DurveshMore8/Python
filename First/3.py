# Write a program to generate the Fibonacci series

length = int(input('Enter length of Fibonacci Series:'))
first = 0
second = 1

print('Fibonacci Series:',end=' ')
print(first,second,end=' ')
for i in range (2, length) :
    sum = first + second
    first = second
    second = sum
    print(sum, end=' ')