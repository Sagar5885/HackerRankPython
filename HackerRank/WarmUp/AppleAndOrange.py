import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    resa = 0
    resb = 0
    for i in apples:
        if(a+i>= s and a+i<= t):
            resa += 1

    for i in oranges:
        if(b+i>= s and b+i<= t):
            resb += 1

    print(resa)
    print(resb)

if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    countApplesAndOranges(s, t, a, b, apple, orange)