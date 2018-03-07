import sys

def countingValleys(s):
    total = 0
    count = 0
    for i in s:
        if(i == "U"):
            count += 1
        else:
            count -= 1

        if(count == 0 and i == "U"):
            total += 1

    return total


if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(s)
    print(result)