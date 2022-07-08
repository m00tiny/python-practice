#!/usr/bin/env python3

def addsubmul(a, b):
    """returns sum, difference and product"""
    sum_ = a + b
    difference = a - b
    product = a * b
    return ("Sum: " + str(sum_) + "\nDifference: " + str(difference) + "\nProduct: " + str(product))


var1 = int(input("First integer: "))
var2 = int(input("Second integer: "))
print(addsubmul(var1, var2))
