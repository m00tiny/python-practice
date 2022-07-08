#!/usr/bin/env python3
M = int(input())
mset = set(map(int, input().split(' ')))

N = int(input())
nset = set(map(int, input().split(' ')))

mdiff = mset.difference(nset)
ndiff = nset.difference(mset)

answer = mdiff.union(ndiff)

for i in sorted(list(answer)):
    print(i)
