def checkSum(board, r, c, dR, dC, n):
    sum = 0
    for i in range(n):
        r += dR
        c += dC

        # out of boundary
        if r < 0 or r >= n or c < 0 or c >= n:
            return sum

        key = str(r) + "-" + str(c)

        if key in board and board[key] == -1:
            return sum
        else:
            sum += 1

    return sum


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    r_q, c_q = input().strip().split(' ')
    r_q, c_q = [int(r_q), int(c_q)]
    r_q = r_q - 1
    c_q = c_q - 1

    board = {}

    for a0 in range(k):
        rObstacle, cObstacle = input().strip().split(' ')
        rObstacle, cObstacle = [int(rObstacle), int(cObstacle)]
        r = rObstacle - 1
        c = cObstacle - 1

        board[str(r) + "-" + str(c)] = -1

    dCList = [-1, -1, -1, 0, 0, 1, 1, 1]
    dRList = [-1, 0, 1, -1, 1, 0, -1, 1]

    sum = 0
    for i in range(8):
        sum += checkSum(board, r_q, c_q, dCList[i], dRList[i], n)

    print(sum)