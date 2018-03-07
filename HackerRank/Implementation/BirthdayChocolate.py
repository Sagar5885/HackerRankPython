def solve(n, s, d, m):
    if(m == 1):
        return s.count(d)
    else:
        count = 0
        for i in range(n):
            res = s[i]
            j = i+1
            if(j+m-1 <= n):
                for k in range(m-1):
                    res = res + s[j+k]
            else:
                break

            if(res == d):
                count = count + 1

        return count



n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
