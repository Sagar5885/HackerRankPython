#Find lcm between two nos
def lcmsol(a):
    lcm = a[0]
    for i in a:
        if(lcm>i):
            num = lcm
            den = i
        else:
            num = i
            den = lcm
        rem = num%den

        while(rem!=0):
            num = den
            den = rem
            rem = num%den

        lcm = int(int(lcm * i) / int(den))

    res = [lcm, den]

    return res

#Find gcd between two element
def gcdsol(a):
    lcm = a[0]
    for i in a:
        if (lcm > i):
            num = lcm
            den = i
        else:
            num = i
            den = lcm
        rem = num % den

        while (rem != 0):
            num = den
            den = rem
            rem = num % den

        lcm = den

    return den

def findMulOfGCDofLCM(a, b):
    i = 1
    res = a
    count = 0
    while(True):
        res = a * i
        if(b%res == 0):
            count = count + 1

        if(res <= b):
            i = i + 1
        else:
            break

    return count



if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    alcm = lcmsol(a)[0]
    bgcd = gcdsol(b)
    print(findMulOfGCDofLCM(alcm, bgcd))