import sys

def pickingNumbers(a):
    adist = list(set(a))
    res = a.count(adist[0])

    for i in adist:
        if(a.count(i)>res):
            res = a.count(i)

    for i in a:
        if (a.__contains__(i + 1)):
            if (res < a.count(i + 1) + a.count(i)):
                res = a.count(i + 1) + a.count(i)
        if (a.__contains__(i - 1)):
            if (res < a.count(i - 1) + a.count(i)):
                res = a.count(i - 1) + a.count(i)

    return res

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = pickingNumbers(a)
    print(result)
