#!/usr/bin/env python3
attempts = int(input())
for i in range(attempts):
    exception_dividers = input().split(' ')
    try:
        print(int(int(exception_dividers[0]) / int(exception_dividers[1])))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero"),e
    except ValueError as v:
        print("Error Code:", v)
