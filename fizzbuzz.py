#!/usr/bin/env python3
#FzzzzzBzzzzz

count = float(0)
for i in range(1, 15):
    count = count + 1
    if (count / 5) ^ 2 == 0 and (count / 3) ^ 2 == 0:
        print("FIZZ BUZZ!")
    elif (count / 5) ^ 2 == 0:
        print("Fizz.")
    elif (count / 3) ^ 2 == 0:
        print("buzz..")
    else:
        print(int(count))
