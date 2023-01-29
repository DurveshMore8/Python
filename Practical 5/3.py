# Write a Python program to sum all the items in a dictionary

dictionary={'a':10, 'b':25, 'c':6, 'd':35, 'e':4, 'f':13, 'g':7}

add = 0
for i in dictionary.values():
    add += i

# Alternate Way
# add = sum(dictionary.values())

print('Addition of all Items of Dictionary is', add)