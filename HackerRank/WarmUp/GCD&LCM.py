
def lcmsol(a, b):
    if(a>b):
        num = a
        den = b
    else:
        num = b
        den = a
    rem = num%den

    while(rem!=0):
        num = den
        den = rem
        rem = num%den

    gcd = den
    lcm = int(int(a * b) / int(gcd))

    return lcm


def gcdsol(a, b):
    if(a>b):
        num = a
        den = b
    else:
        num = b
        den = a
    rem = num%den

    while(rem!=0):
        num = den
        den = rem
        rem = num%den

    return den

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))

    lcm = lcmsol(a[0], a[1])
    gcd = gcdsol(a[0], a[1])
    for i in a:
        lcm = lcmsol(lcm, i)
        gcd = gcdsol(gcd, i)

    print(lcm)
    print(gcd)

    lcmb = lcmsol(b[0], b[1])
    gcdb = gcdsol(b[0], b[1])
    for i in b:
        lcmb = lcmsol(lcmb, i)
        gcdb = gcdsol(gcdb, i)

    print(lcmb)
    print(gcdb)

