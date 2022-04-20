#!/usr/bin/python

import whois as who
# A test for whois lookups

data = raw_input('')
w = who.query(data)

print w
