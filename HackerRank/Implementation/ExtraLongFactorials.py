def extraLongFactorials(n):
    res = 1
    for i in range(n):
        res = res * (i + 1)
    print(res)


if __name__ == "__main__":
    n = int(input().strip())
    extraLongFactorials(n)
