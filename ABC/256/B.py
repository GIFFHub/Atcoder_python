if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    P = 0  # 点数
    base = [0]*8
    base[0] = 1

    for i in range(N):
        progress = min(A[i], 4)  # ベース進む数
        for j in reversed(range(4)):
            base[j+progress] = base[j]
            if j > 0:
                base[j] = 0

        P += sum(base[4:])
        for k in range(4, 8):
            base[k] = 0

    print(P)

