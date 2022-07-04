#!/usr/bin/env python3

# This code turns camelCase input into snake_case output.

# our pseudo-input
camelCase = 'thisIsCamelCase'

def snake_case(string):
    # pull each character into a list
    camel_case = [i for i in camelCase]

    # just build a whole new string for now
    permutate = list()

    # iterate through the list, moving the first character
    # to the back, meanwhile checking for UpperCase
    # characters and adding an _underscore as well as 
    # lowercasing the character to the back
    for char in camel_case:
        if char.isupper() is True:
            permutate.append('_')
            permutate.append(char.lower())
        else:
            permutate.append(char)
    return ''.join(permutate)

print(snake_case(camelCase))
