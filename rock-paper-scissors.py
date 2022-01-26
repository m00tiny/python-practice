#!/usr/bin/env python3

import random
import sys

print("Rock, Paper, Scissors.")

# Track wins, losses, ties
wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print('(r)ock, (p)aper, (s)cissors or (q)uit?')
        playerChoice = input()
        if playerChoice == 'q':
            sys.exit()
        if playerChoice == 'r' or playerChoice == 'p' or playerChoice == 's':
            break
        print('Choose r, p, s or q.')
    if playerChoice == 'r':
        print('Rock versus...')
    if playerChoice == 'p':
        print('Paper versus...')
    if playerChoice == 's':
        print('Scissors versus...')

    computerMove = random.randint(1, 3)
    if computerMove == 1:
        computerMove = 'r'
        print('Rock!')
    if computerMove == 2:
        computerMove = 'p'
        print('Paper!')
    if computerMove == 3:
        computerMove = 's'
        print('Scissors!')

    if playerChoice == computerMove:
        print("It\'s a tie!")
        ties = ties + 1
    elif playerChoice == 'r' and computerMove == 's':
        print('You win! Rock smashes scissors.')
        wins = wins + 1
    elif playerChoice == 'p' and computerMove == 'r':
        print('You win! Paper covers rock.')
        wins = wins + 1
    elif playerChoice == 's' and computerMove == 'p':
        print('You win! Scissors cut paper.')
        wins = wins + 1
    elif playerChoice == 'r' and computerMove == 'p':
        print('You lose! Paper covers rock.')
        losses = losses + 1
    elif playerChoice == 'p' and computerMove == 's':
        print('You lose! Scissors cut paper.')
        losses = losses + 1
    elif playerChoice == 's' and ComputerMove =='r':
        print('You lose! Rock smashes scissors.')
        losses = losses + 1

