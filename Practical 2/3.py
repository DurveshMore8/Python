# Define a procedure histogram() that takes a list of integer and prints a histogram to the screen.
# For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******

def histogram(listt):
    for i in listt:
        for j in range(0, i):
            print('*', end='')
        print()

histogram([5, 4, 9, 1])