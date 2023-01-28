

if __name__ == '__main__':
    H, W = map(int, input().split())
    A = []
    m = 101
    for _ in range(H):
        A.append(list(map(int, input().split())))

    for i in range(H):
        for j in range(W):
            m = min(m, A[i][j])
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - m

    print(ans)


