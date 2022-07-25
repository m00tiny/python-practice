#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    sum_a = list()
    sum_b = list()
    backtick = n
    for i in range(n):
        backtick -= 1
        sum_a.append(arr[i][i])
        sum_b.append(arr[i][backtick])
    result = abs(sum(sum_a) - sum(sum_b))
    return result

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

