import sys

def sockMerchant(ar):
    d = {}
    for i in ar:
        if(i in d):
            d[i] += 1
        else:
            d[i] = 1

    count = 0
    for i in d:
        if(d[i]>1):
            count += int(d[i]/2)

    return count

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(ar)
print(result)