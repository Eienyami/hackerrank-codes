#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

c.sort()
i=0
count=0

    if c[i]==c[i+1]:
        i+=2
        count+=1
        print i
        
print count
