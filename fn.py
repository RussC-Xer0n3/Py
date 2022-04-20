#!/usr/bin/env python

# Simple to increment alpha values.
# @author Russell Clarke aka Rusher SD200984
# @version 1.5
# @Created 21.12.2018
# @Listening to Talvin Singh

a1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'q', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def increaser(a):
    for i in a:
        for j in a:
            print("." + j + i)
            
def increaserThree(a):
    for i in a:
        for j in a:
            for k in a:
                print("." + k + j + i)

print("First the binarys: \r\n")
increaser(a1)
print("\r\n")
print("Now the Ternaries: \r\n")
increaserThree(a1)

exit(0)
