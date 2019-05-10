#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    cou = 0
    a = max(ar)
    for i in ar:
        if (i == a):
            cou += 1
    return cou        
            

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
