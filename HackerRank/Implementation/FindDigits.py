def findDigits(n):
    count = 0
    for d in str(n):
        if(int(d) != 0):
            if(n%(int(d)) == 0):
                count = count + 1

    return count

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = findDigits(n)
        print(result)
