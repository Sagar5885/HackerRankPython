import sys

def getMoneySpent(keyboards, drives, s):
    res = -1
    possibleCost = list()
    for k in keyboards:
        for d in drives:
            possibleCost.append(k+d)

    possibleCost.sort()

    for i in possibleCost:
        if(i <= s):
            res = i
        else:
            break

    return res

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)