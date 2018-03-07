import sys

def staircase(n):
    i=0
    while(i<n):
        tmp = i
        tmp1 = n-i-1
        while(tmp1>0):
            print(' ', end='')
            tmp1 -= 1
        while(tmp>=0):
            print('#', end='')
            tmp -= 1
        print()
        i += 1

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
