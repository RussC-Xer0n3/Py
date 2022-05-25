#! /usr/bin/env python3
# Xer0n3 - 25.05.2022
# version 0.3

import math

# equilaterally, h is half any hypotenuse where the bits sum to 24
# l defines the entire hypotenuse
# their exponents denote the total quantity of the equilateral
# the sum p refers to sumising the components 
float h = pow(24.000, 12)
float l = pow(32.000, 6)



float p = sum(h, l)

## EXPERIMENTAL ##
# apply proc to polygons
def proc(h, l, p):
    # for the equilateral exponents of the sum of the individual components
    # tell the remainder the sum is subtracted from the total of exponents ternerilateraly 
    for i in p:

        (h%l) == ((h,l) - p)
        return

