#!/bin/python3

import sys

def solve(n, p):
    if(p<=(n-p)):
        return int(p/2)
    else:
        if(n%2 == 0 and p%2 != 0):
            return int((n-p)/2)+1
        else:
            return int((n-p)/2)

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
