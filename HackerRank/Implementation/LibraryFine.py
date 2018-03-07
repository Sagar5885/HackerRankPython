def libraryFine(d1, m1, y1, d2, m2, y2):
    if(y2<y1):
        return 10000
    elif(y2>y1):
        return 0
    else:
        if(m2<m1):
            return (m1-m2)*500
        elif(m2>m1):
            return 0
        else:
            if(d1>d2):
                return (d1-d2)*15
            else:
                return 0


if __name__ == "__main__":
    d1, m1, y1 = input().strip().split(' ')
    d1, m1, y1 = [int(d1), int(m1), int(y1)]
    d2, m2, y2 = input().strip().split(' ')
    d2, m2, y2 = [int(d2), int(m2), int(y2)]
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    print(result)
