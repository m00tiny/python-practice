#!/usr/bin/env python3

def is_leap(year):
    leap = False
    check_leap = ((year // 400) % 2)
    if check_leap == 0:
        check_leap = ((year // 100) % 2)
        if check_leap == 0:
            return leap
        else:
            check_leap = ((year // 4) % 2)
            if check_leap == 0:
                leap = True
    return leap

year = int(raw_input())
print is_leap(year)
