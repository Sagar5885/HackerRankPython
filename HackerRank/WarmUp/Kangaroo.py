import sys

import math


def kangaroo(x1, v1, x2, v2):
    if(v1-v2>0):
        if((math.fabs((x2 - x1) % (v1 - v2))) == 0):
            return str("YES")
        else:
            return str("NO")
    else:
        return str("NO")


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)