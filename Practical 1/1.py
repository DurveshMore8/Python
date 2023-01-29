# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input('Enter Name:')
age = int(input('Enter Age:'))
print(name+', you will turn 100 year old in '+str(100-age)+' years')