import sys

def miniMaxSum(arr):
    arr.sort();
    min = 0
    max = 0
    i=0
    while(i<arr.__len__()):
        if(i != 0):
            max += arr[i]
        if(i != arr.__len__()-1):
            min += arr[i]
        i += 1

    print(min, max)

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
