#!/usr/bin/env python3
# chess
import itertools
def theBoard():
    light_square = "|   |"
    dark_square = "|____|"
    ranks = ["1", "2", "3", "4", "5", "6", "7", "8"]
    files = ["a", "b", "c", "d", "e", "f", "g", "h"]
    x = itertools.product(ranks, files)
    squares = [x for x in x]
    i = range(1, 9)
    for i in squares:
        print(i)

theBoard()
