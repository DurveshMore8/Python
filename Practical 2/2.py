# Define a function that computes the length of a given list or string.

def length(data):
    count = 0
    for i in data:
        count += 1
    return count

# For String
string = input('Enter String: ')
print(length(string))

# For List
listt = ['Hello', 'World', 1, 2, 3]
print(length(listt))