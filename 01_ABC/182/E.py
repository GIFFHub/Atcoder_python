

if __name__ == '__main__':
    H, W, N, M = map(int, input().split())
    obj = [[0]*W for _ in range(H)]
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
        obj[a-1][b-1] = 1

    C = []
    D = []
    for _ in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
        obj[c-1][d-1] = -1

    table = [[False]*W for _ in range(H)]
    # 右方向
    for i in range(H):
        flg = 0
        for j in range(W):
            if obj[i][j] == 1:
                flg = 1
                table[i][j] = True
            elif obj[i][j] == -1:
                flg = 0
            else:
                if flg:
                    table[i][j] = True

    # 左方向
    for i in range(H):
        flg = 0
        for j in range(W):
            j = W-j-1
            if obj[i][j] == 1:
                flg = 1
                table[i][j] = True
            elif obj[i][j] == -1:
                flg = 0
            else:
                if flg:
                    table[i][j] = True

    # 下方向
    for j in range(W):
        flg = 0
        for i in range(H):
            if obj[i][j] == 1:
                flg = 1
                table[i][j] = True
            elif obj[i][j] == -1:
                flg = 0
            else:
                if flg:
                    table[i][j] = True

    # 上方向
    for j in range(W):
        flg = 0
        for i in range(H):
            i = H-i-1
            if obj[i][j] == 1:
                flg = 1
                table[i][j] = True
            elif obj[i][j] == -1:
                flg = 0
            else:
                if flg:
                    table[i][j] = True
    ans = 0
    for i in range(H):
        ans += table[i].count(True)
    print(ans)
