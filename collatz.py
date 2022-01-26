#!/usr/bin/env python3

# collatz function

print("Give me a number.")
collatznum = int(input())

def collatz(collatznum):
    while collatznum != 1:
        checkCollatz = collatznum % 2
        if checkCollatz == 0:
            print(str(collatznum) + " is even.")
            collatznum = collatznum // 2
        elif checkCollatz == 1:
            print(str(collatznum) + " is odd.")
            collatznum = 3 * collatznum + 1
    if collatznum == 1:
        print("Finished. " + str(collatznum) + " has reached 1.")
collatz(collatznum)
