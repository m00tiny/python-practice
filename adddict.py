#!/usr/bin/env python3
text = input()

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 1
        else:
            result[letter] += 1
    return(result)

print(count_letters(text))
