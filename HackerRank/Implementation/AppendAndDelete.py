def appendAndDelete(s, t, k):
    lenOfEqual = 0
    if(s<t):
        n = s.__len__()
    else:
        n = t.__len__()

    for i in range(n):
        if(s[i] == t[i]):
            lenOfEqual = lenOfEqual + 1
        else:
            break

    if((s.__len__()+t.__len__()-(2*lenOfEqual)) > k):
        return "No"
    elif((s.__len__()+t.__len__()-(2*lenOfEqual))%2 == k%2):
        return "Yes"
    elif((s.__len__()+t.__len__()-k)<0):
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    print(result)
