#!/usr/bin/env python3
# The defaultdict tool is a container in the collections class of
#  Python. It's similar to the usual dictionary (dict) container,
#  but it has one difference: The value fields' data type is
#  specified upon initialization.
from collections import defaultdict

d = defaultdict(list)
list1 = []
n, m = map(int, input().split())
for i in range(1, n + 1):
    d[input()].append(str(i))


for i in range(m):
    b = input()
    if b in d:
        print(' '.join(d[b]))
    else:
        print(-1)
