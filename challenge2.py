# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

entry = set(input('Enter your text: '))

vowels = frozenset("aeiou")
vowels = {'a', 'e', 'i', 'o', 'u'}

print(sorted(entry - vowels))