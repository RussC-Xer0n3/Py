#!/usr/bin/env python

# Simple port incrementer
# @author Russell Clarke aka Rusher SD200984
# @version 1.5
# @Created 21.12.2018
# @Listening to Talvin Singh

c = ':'

def port(c):
	for i in range(65526):
		j = str(i)
		print(c +j)
		
port(c)

exit(0)
