#!/usr/bin/env python3
import numpy

np.set_printoptions(legacy='1.13')
A = np.array(input().split(), float)
print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))