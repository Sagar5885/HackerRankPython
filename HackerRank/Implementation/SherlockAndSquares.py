import math

def squares(a, b):
    start = int(math.sqrt(a));
    count = 0

    while(math.pow(start, 2) <= b):
        if(math.pow(start, 2) >= a):
            count = count + 1
        start = start + 1

    return count

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        a, b = input().strip().split(' ')
        a, b = [int(a), int(b)]
        result = squares(a, b)
        print(result)
