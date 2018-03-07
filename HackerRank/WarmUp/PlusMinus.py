def plusMinus(arr):
    a = 0
    b = 0
    c = 0
    for i in arr:
        if(i>0):
            a += 1
        if(i<0):
            b += 1
        if(i == 0):
            c += 1

    print(a/arr.__len__())
    print(b/arr.__len__())
    print(c/arr.__len__())

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)