if __name__ == '__main__':
    N = int(input())
    A = []
    B = []
    C = []
    D = []
    for _ in range(N):
        a, b, c, d = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)
    min_x = min(A)
    max_x = max(B)
    min_y = min(C)
    max_y = max(D)
    ans = 0
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            for i in range(N):
                if A[i] <= x < B[i] and C[i] <= y < D[i]:
                    ans += 1
                    break
    print(ans)

