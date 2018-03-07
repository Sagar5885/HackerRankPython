def permutationEquation(p, n):
    result = list()
    for i in range(n):
        tmp1 = p.index(i+1)
        tmp2 = p.index(tmp1+1)
        result.append(tmp2+1)

    return result


if __name__ == "__main__":
    n = int(input().strip())
    p = list(map(int, input().strip().split(' ')))
    result = permutationEquation(p, n)
    print("\n".join(map(str, result)))