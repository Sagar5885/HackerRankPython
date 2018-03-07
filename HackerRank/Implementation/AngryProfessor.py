#!/bin/python3

import sys

def angryProfessor(k, a):
    count = 0
    for i in a:
        if(i <= 0):
            count = count + 1

    if(count >= k):
        return "NO"
    else:
        return "YES"

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        a = list(map(int, input().strip().split(' ')))
        result = angryProfessor(k, a)
        print(result)
