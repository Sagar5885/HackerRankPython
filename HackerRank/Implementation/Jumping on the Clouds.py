def jumpingOnClouds(n, c, k):
    i = 0
    e = 100
    while(i<n):
        if(c[i] == 1):
            e = e - 2

        e = e - 1
        i = i + k

    return e

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    c = list(map(int, input().strip().split(' ')))
    result = jumpingOnClouds(n, c, k)
    print(result)
