#!/bin/python3

import sys

def timeConversion(s):
    no = int(s[0]+s[1])
    if((s[8:]).__eq__("PM") & (no != 12)):
        return str(no+12)+s[2:-2]
    elif((s[8:]).__eq__("AM") & (no == 12)):
        return "00"+s[2:-2]
    else:
        return s[:-2]

s = input().strip()
result = timeConversion(s)
print(result)
