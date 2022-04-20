#!/usr/bin/env python
# @author Russell Clarke aka Rusher SD200984
# @version 1.0
# @Created 22.12.2018

reg = ['^A-z0-9']
uDef = 257

def padd(x, y):
    for i in range(0, 99999999999):
        for x in range(i, y):
            p = x+=x
            return p

padd(reg, uDef)
exit(0)