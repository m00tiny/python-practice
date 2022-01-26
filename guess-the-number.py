#!/usr/bin/env python3

# number guessing game
import random
import sys

goal = random.randint(1, 100)
guessCount = 0

print ("I'm thinking of a number between 1 and 100.")

# accept up-to 10 guesses from player
while guessCount < 10:
    print("Take a guess: ")
    guess = int(input())
    guessCount = guessCount + 1

    if guess < goal:
        print("Too low!")
    elif guess > goal:
        print("Too high!")
    elif guess == goal:
        print("About time! You figured it out in only " + str(guessCount) + " guesses.")
        sys.exit()
    else:
        print("You're out of guesses! The number I thought of was: " + str(goal) + ".")
