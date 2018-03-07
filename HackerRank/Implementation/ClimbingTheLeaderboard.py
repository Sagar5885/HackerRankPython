import sys

def climbingLeaderboard(scores, alice):
    #result = list()
    scores.sort(reverse=True)
    d = {}
    k = 1
    for i in scores:
        if (i not in d):
            d[i] = k
            k = k + 1

    for i in alice:
        if(i < min(scores)):
            #result(d[min(scores)] + 1)
            print(d[min(scores)] + 1)
        else:
            for j in d:
                if(i > j or i == j):
                    #result(d[j])
                    print(d[j])
                    break


    #return result

if __name__ == "__main__":
    n = int(input().strip())
    scores = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    alice = list(map(int, input().strip().split(' ')))
    result = climbingLeaderboard(scores, alice)
    #print ("\n".join(map(str, result)))


