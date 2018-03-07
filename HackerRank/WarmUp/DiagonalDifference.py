import sys

def diagonalDifference(a, n):
    d1 = 0
    d2 = 0
    i = 0
    while(i<n):
        d1 += a[i][i]
        d2 += a[i][n-i-1]
        i += 1

    return abs(d1-d2)

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a, n)
    print(result)