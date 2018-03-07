import sys

def birthdayCakeCandles(n, ar):
    m = max(ar)
    res = 0
    for i in ar:
        if(i == m):
            res += 1

    return res

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)