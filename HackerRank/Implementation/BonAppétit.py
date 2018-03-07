def BonAppSol(n, ar, k, b):
    totalsplit = 0
    for i in range(int(n)):
        if(i != int(k)):
            totalsplit = totalsplit + ar[i]

    annasPortion = totalsplit/2

    if(annasPortion == b):
        print("Bon Appetit")
    else:
        print(str(int(b-annasPortion)))

n, k = input().strip().split(' ')
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
BonAppSol(n, ar, k, b)