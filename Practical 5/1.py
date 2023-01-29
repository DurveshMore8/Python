# Write a Python script to sort (ascending and descending) a dictionary by value

dictionary = {4:'h', 6:'n', 1:'p', 5:'o', 3:'t', 2:'y'}

print('Dictionary Before Sorting: ')
for i, j in dictionary.items():
    print(i, ':', j)

print('Dictionary Sorted in Ascending Order: ')
for i, j in sorted(dictionary.items()):
    print(i, ':', j)

print('Dictionary Sorted in Descending Order: ')
for i, j in sorted(dictionary.items(), reverse = True):
    print(i, ':', j)