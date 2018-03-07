#!/bin/python3

import sys

def utopianTree(n):
    res = 1
    if(n>0):
        for i in range(n):
            if(i%2 == 0):
                res = res * 2
            else:
                res = res + 1

    return res

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = utopianTree(n)
        print(result)
