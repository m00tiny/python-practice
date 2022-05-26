#!/usr/bin/env python3
#####################################
# HackerRank camelCase 4 challenge ##
# YOU ARE MISSING A LINE BREAK AT  ##
# THE END OF ONE OF THE TEST CASES ##
# .rstrip IS WHAT YOU WANT         ##
#####################################
import re
while True:
    try:
        # DO NOT MISS THIS COMMENT
        # THIS IS THE SOLUTION .rstrip
        # one of the test cases has a LINE
        # BREAK at the end ^_^ see?
        # YOU WANT TO USE .rstrip
        s = input().rstrip()
        #            _        _
        #   _ __ ___| |_ _ __(_)_ __
        #  | '__/ __| __| '__| | '_ \
        # _| |  \__ \ |_| |  | | |_) |
        #(_)_|  |___/\__|_|  |_| .__/
        #                      |_|
        combinesplit, MVC, parenths = s.split(";")
        if combinesplit == "S":
            if MVC == "M":
                cap = parenths[:-2]

            if MVC == "V" or MVC == "C":
                cap = parenths

            combinesplit = re.sub ("(\w)([A-Z])", r"\1 \2", cap)
            print (combinesplit.lower())

        if combinesplit == "C":
            cap = parenths.title ()
            combinesplit = re.sub (r" ", r"", cap)
            q = combinesplit[:1].lower() + combinesplit[1:]

            if MVC == "M":
                print (q+"()")

            if MVC == "V":
                print (combinesplit)

            if MVC == "C":
                print (q)

    except EOFError:
        break
