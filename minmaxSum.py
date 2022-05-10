#!/usr/bin/env Python3

import math
import os
import random
import re
import sys

#
# Complete the minMaxSum function below
#
# The function accepts INTEGER_ARRAY arr as a parameter
#

def minMaxSum(arr):
    arr.sort()
    min = sum(arr) - arr[4]
    max = sum(arr) - arr[0]
    print ("" + str(min) + " " + str(max) + "")

if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5]

    minMaxSum(arr)
