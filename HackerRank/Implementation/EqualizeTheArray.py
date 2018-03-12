def equalizeArray(arr):
    s = set(arr)
    count = 0
    for i in s:
        tmp = arr.count(i)
        if(tmp > count):
            count = tmp

    return arr.__len__() - count

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = equalizeArray(arr)
    print(result)
