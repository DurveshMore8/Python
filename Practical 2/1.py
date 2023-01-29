# Write a function that takes a character (i.e., a string of length 1) and return True if it is a vowel, False otherwise.

def vowel(char):
    vowels = ['a','e','i','o','u']
    for i in vowels:
        if char.lower() == i:
            return True
    return False

character = input('Enter One Alphabet: ')
print(vowel(character))