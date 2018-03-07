#Lenghthy approach with actual array rotation
# def circularArrayRotation(a, k, m):
#     if (k < a.__len__()):
#         for i in range(k):
#             oneRotation(a)
#     elif (k == a.__len__()):
#         print()
#     else:
#         knew = k % n
#         for i in range(knew):
#             oneRotation(a)
#
#     result = list()
#     for i in m:
#         result.append(a[i])
#
#     return result
#
# def oneRotation(a):
#     i = a.__len__()-1;
#     tmp = a[i]
#     while(i>0):
#         a[i] = a[i-1]
#         i = i - 1
#
#     a[0] = tmp

#Faster approach with pure maths
def circularArrayRotation1(a, k, m):
    result = list()
    for i in m:
        result.append(a[(i-k)%(a.__len__())])

    return result


if __name__ == "__main__":
    n, k, q = input().strip().split(' ')
    n, k, q = [int(n), int(k), int(q)]
    a = list(map(int, input().strip().split(' ')))
    m = []
    m_i = 0
    for m_i in range(q):
       m_t = int(input().strip())
       m.append(m_t)
    result = circularArrayRotation1(a, k, m)
    print ("\n".join(map(str, result)))


