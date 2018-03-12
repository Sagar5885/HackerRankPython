def jumpingOnClouds(c, n):
    count = 0
    i = 0
    while(i<n):
        if(i+2 < n):
            if(c[i+2] == 0):
                i = i + 2
                count = count + 1
            else:
                i = i + 1
                count = count + 1
        elif(i+1 < n):
            i = i + 1
            count = count + 1
        else:
            break

    return count

if __name__ == "__main__":
    n = int(input().strip())
    c = list(map(int, input().strip().split(' ')))
    result = jumpingOnClouds(c, n)
    print(result)
