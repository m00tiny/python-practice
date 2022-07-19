#!/usr/bin/env python3
# detect if input is a float
# hackerrank solution

def check_user_input(var):
    try:
        val = int(var)
        print("False")
    except ValueError:
        try:
          val = float(var)
          print("True")
        except ValueError:
            print("False")


T = int(input())
for i in range(T):
    check_user_input(input())
