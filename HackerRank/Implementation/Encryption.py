import sys
from math import ceil, sqrt

if __name__ == "__main__":
    s = input().strip()
    c = ceil(sqrt(len(s)))
    print(' '.join(map(lambda x: s[x::c], range(c))))
