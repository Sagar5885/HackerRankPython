def taumBday(b, w, x, y, z):
    if((z+x) < y):
        wc = w * (z+x)
    else:
        wc = w * y

    if((z+y) < x):
        bc = b * (z+y)
    else:
        bc = b * x

    return (wc + bc)

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        b, w = input().strip().split(' ')
        b, w = [int(b), int(w)]
        x, y, z = input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = taumBday(b, w, x, y, z)
        print(result)
