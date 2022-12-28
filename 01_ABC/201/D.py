

if __name__ == '__main__':
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        tmp = []
        S = input()
        for s in S:
            if s == '+':
                tmp.append(1)
            else:
                tmp.append(-1)
        A.append(tmp)

    opt = [[0]*W for _ in range(H)]

    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):

            if (i+j) % 2 == 0:
                if i == H - 1 and j == W - 1:
                    continue
                if i == H - 1:
                    opt[i][j] = opt[i][j+1] + A[i][j+1]
                    continue
                if j == W - 1:
                    opt[i][j] = opt[i+1][j] + A[i+1][j]
                    continue
                opt[i][j] = max(opt[i+1][j] + A[i+1][j], opt[i][j+1] + A[i][j+1])

            else:
                if i == H - 1 and j == W - 1:
                    continue
                if i == H - 1:
                    opt[i][j] = opt[i][j+1] - A[i][j+1]
                    continue
                if j == W - 1:
                    opt[i][j] = opt[i+1][j] - A[i+1][j]
                    continue
                opt[i][j] = min(opt[i+1][j] - A[i+1][j], opt[i][j+1] - A[i][j+1])

    if opt[0][0] > 0:
        ans = 'Takahashi'
    elif opt[0][0] < 0:
        ans = 'Aoki'
    else:
        ans = 'Draw'
    print(ans)