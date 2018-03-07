import sys

def simpleArraySum(n, ar):
    res = 0
    for i in ar:
        res += i
    return res

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
