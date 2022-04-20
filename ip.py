#!/usr/bin/env python

# Should return an IP address
# @author Russell Clarke aka Rusher SD200984
# @version 1.4
# @Created 21.12.2018
# @Listening to Talvin Singh

d = '.'

for i in range(255):
    for j in range(255):
        for k in range(255):
            for l in range(255):
                a = str(l)
                b = str(k)
                c = str(j)
                e = str(i)
                print(a + d + b + d + c + d + e)

exit(0)
