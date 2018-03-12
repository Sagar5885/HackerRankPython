def camelcase(s):
    count = 0
    for i in range(s.__len__()):
        if(s[i].isupper()):
            count = count + 1

    return count+1

if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)
