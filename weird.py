#!/usr/bin/env python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    weird = [6,8,10,12,14,16,18,20]
    if n % 2 != 0:
        print ("Weird");
    elif n in weird:
        print ("Weird");
    else:
		print ("Not Weird");
