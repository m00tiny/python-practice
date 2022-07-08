#!/usr/bin/env python3
from itertools import combinations_with_replacement

incoming = input().split(' ')
S = incoming[0]
k = int(incoming[1])
for x in combinations_with_replacement(sorted(S), k):
    print(''.join(x))

