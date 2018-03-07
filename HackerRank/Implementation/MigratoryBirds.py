import sys

def migratoryBirds(ar):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    countres = 1
    for i in ar:
        if (i == 1):
            count1 = count1 + 1
        if (i == 2):
            count2 = count2 + 1
        if (i == 3):
            count3 = count3 + 1
        if (i == 4):
            count4 = count4 + 1
        if (i == 5):
            count5 = count5 + 1

    count = count1
    if (count2 > count):
        countres = 2
        count = count2
    if (count3 > count):
        countres = 3
        count = count3
    if (count4 > count):
        countres = 4
        count = count4
    if (count5 > count):
        countres = 5

    return countres


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(ar)
print(result)