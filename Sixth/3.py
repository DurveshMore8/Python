# Write a Python program to read last n lines of a file.

obj = open('D://Practicals//Python//Text_Files//2nd.txt', 'r')

n = int(input('Enter the number of last line to read: '))
 
lineslist = obj.readlines()     #Read all Lines of File
textline = lineslist[-n:]       #Concept of Negative Indexing

print('Text in Last', n, 'Lines:')
for i in textline:
    print(i, end = '')

obj.close()