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
        combinesplit, mvc, parenth = s.split(";")
        if combinesplit == "S":
            if mvc == "M":
                capitalize = parenth[:-2]                                   
                
            if mvc == "V" or mvc == "C":
                capitalize = parenth
            
            s = re.sub ("(\w)([A-Z])", r"\1 \2", capitalize)
            print (s.lower())
                
        if combinesplit == "C":
            capitalize = parenth.title ()
            s = re.sub (r" ", r"", capitalize)
            q = s[:1].lower() + s[1:]                
            
            if mvc == "M":                                
                print (q+"()")
                
            if mvc == "V":
                print (s)
              
            if mvc == "C":
                print (q)
            
    except EOFError:
        break