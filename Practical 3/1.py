# A pangram is a sentence that contains all the letters of the English alphabet at least once,
# for example, The quick brown fox jumps over the lazy dog.
# Your task here is to write a function to check a snetence to see if it is a pangram or not.

def pangram(sentence):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabets:
        if letter not in sentence.lower():
            return False
    return True

print(pangram('The quick brown fox jumps over the lazy dog'))