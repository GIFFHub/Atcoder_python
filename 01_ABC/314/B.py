

if __name__ == '__main__':
    N = int(input())
    C = []
    A = []
    for _ in range(N):
        C.append(int(input()))
        A.append(set(map(int, input().split())))

    # 当たりの目
    X = int(input())

    # 当たった人の番号リスト(-1)
    atari = []
    for i, a in enumerate(A):
        if X in a:
            atari.append(i)

    # 当たってる人の中で最も少なく賭けた目の個数
    C_min = 37
    for ata in atari:
        C_min = min(C_min, C[ata])

    # 少なく賭けた人たちの洗い出し
    ans = []
    for ata in atari:
        if C[ata] == C_min:
            ans.append(ata+1)

    print(len(ans))
    print(*ans)





