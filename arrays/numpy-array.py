#!/usr/bin/env python3
# take a list of input, turn into numpy array
# return a reverse numpy array
# sounds, dump, what's the point?
import numpy

file = open('input/input00.txt', 'r')
incoming = file.readline().split(' ')
outgoing = numpy.array(incoming[::-1], float)

print(outgoing)
