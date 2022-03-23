#!/usr/bin/env python3
n = int(5)
arr = [2, 3, 6, 6, 5]
winner = max(arr)
runnerup = winner
runnerup = runnerup - 1
if runnerup in arr:
    print (runnerup)
else:
    while runnerup in arr == False:
        runnerup = runnerup -1
    print(runnerup)
