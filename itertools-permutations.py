#!/usr/bin/env python3

from itertools import permutations
s,n = ("HACK", 2)
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')
