import sys

def breakingRecords(score):
    highest = score[0]
    lowest = score[0]

    hcount = 0
    lcount = 0
    for i in score:
        if(i>highest):
            highest = i
            hcount = hcount + 1
        if(i<lowest):
            lowest = i
            lcount = lcount + 1

    return [hcount, lcount]


if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))


