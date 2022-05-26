#! /usr/bin/env python3
# Xer0n3 - 25.05.2022
# version 0.5

import math

# equilaterally, h is half any hypotenuse where the bits sum to 24
# l defines the entire hypotenuse
# their exponents denote the total quantity of the equilateral
# the sum p refers to sumising the components
# c tell the components where the corners are programatically
float h = pow(24.000, 12)
float l = pow(32.000, 6)
float c = pow(8, 4)

float p = sum(h, l)

## EXPERIMENTAL ##
# apply proc to polygons
def proc(h, l, c, p):
    # for the equilateral exponents of the sum of the individual components
    # tell the remainder the sum is subtracted from the total of exponents ternerilateraly
    # tell it how to shut down in regression c = close and closing the tangent

    c = lambda c:tan(h,l,c,p)
    
    for i in p:
        try:
            c += (-x)
            x = (h%l) == ((h,l) - p)
        except:
            c == exit
        return

