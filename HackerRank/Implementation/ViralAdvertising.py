def viralAdvertising(n):
    res = 5
    likeCount = 2
    if(n>1):
        i = 2
        while(i <= n):
            res = int(res/2) * 3
            likeCount = likeCount + int(res / 2)
            i = i + 1

    return likeCount

if __name__ == "__main__":
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)
