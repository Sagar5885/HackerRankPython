def nonDivisibleSubset(k, arr):
    counts = [0] * k
    for number in arr:
        counts[number % k] += 1

    count = min(counts[0], 1)
    for i in range(1, k // 2 + 1):
        if i != k - i:
            count += max(counts[i], counts[k - i])
    if k % 2 == 0:
        count += 1

    return count

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = nonDivisibleSubset(k, arr)
    print(result)
