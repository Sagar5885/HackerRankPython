import math

def beautifulDays(i, j, k):
    res = 0
    while(i <= j):
        tmp = reverse(i)
        if((math.fabs(tmp - i)) % k == 0):
            res = res + 1
        i = i + 1

    return res

def reverse(num):
  return int(str(num)[::-1])

if __name__ == "__main__":
    i, j, k = input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautifulDays(i, j, k)
    print(result)
