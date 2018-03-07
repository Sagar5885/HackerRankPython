def cutTheSticks(arr, n):
    result = set()
    result.add(n)
    m = min(arr)
    start = m
    while(True):
        count = 0
        for i in arr:
            if(i-start > 0):
                count = count + 1
        if(count != 0):
            result.add(count)
        else:
            break
        start = start + 1

    return sorted(result, reverse=True)

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = cutTheSticks(arr, n)
    print ("\n".join(map(str, result)))


