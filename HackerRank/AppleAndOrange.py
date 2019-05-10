#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))
acount=0
ocount=0
for i in apple:
    if a+i in (s,t):
        acount+=1
      
    
for i in orange:
    if b+i in (s,t):
        ocount+=1
        
        
print acount
print ocount
