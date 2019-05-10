#!/bin/python

import sys


n = int(raw_input().strip())
for a0 in xrange(n):
    i = int(raw_input().strip())
    # your code goes here
    if i < 38:
        pass
    elif i%5==3:
        i+=2
    elif i%5==4:
        i+=1
    else:
        pass
    print i
