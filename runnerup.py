#!/usr/bin/env python3
n = int(5)
arr = [2, 3, 6, 6, 5]
winner = max(arr)
runnerup = winner - 1
if runnerup not in arr:
    runnerup = runnerup -1
print(runnerup)
