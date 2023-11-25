

if __name__ == '__main__':
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input())

    # 各行の丸の数
    G = []
    for s in S:
        G.append(s.count('o'))

    R = [0]*N
    # 各列の丸の数
    for s in S:
        for i in range(N):
            if s[i] == 'o':
                R[i] += 1


    ans = 0
    for x in range(N):
        for y in range(N):
            if S[x][y] == 'o':
                if G[x] - 1 > 0:
                    if R[y] - 1 > 0:
                        ans += (G[x]-1)*(R[y]-1)

    print(ans)




