#!/usr/bin/env python3
# the lonely integer hackerrank solution
from collections import Counter

def lonelyinteger(integer, array):
    for i in array:
        if array.count(i) == 1:
            return i
        else:
            continue


n = int(4)
a = [1, 2, 3, 4, 3, 2, 1]
print(lonelyinteger(n, a))
