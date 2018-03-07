import sys
import math

def solve(grades):
    res = []
    for i in grades:
        if (i > 37):
            if(((int(math.ceil(i / 5.0)) * 5)-i) < 3):
                res.append(int(math.ceil(i / 5.0)) * 5)
            else:
                res.append(i)
        else:
            res.append(i)

    return res


n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
