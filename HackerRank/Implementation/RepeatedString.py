def repeatedString(s, n):
    count = 0
    if(s.__len__()>1):
        acount = s.count('a')
        tmp1 = n//s.__len__()
        tmp2 = n%s.__len__()

        count = tmp1 * acount
        for i in range(tmp2):
            if(s[i] == 'a'):
                count = count + 1
    else:
        if(s[0] == 'a'):
            count = n

    return count

if __name__ == "__main__":
    s = input().strip()
    n = int(input().strip())
    result = repeatedString(s, n)
    print(result)
