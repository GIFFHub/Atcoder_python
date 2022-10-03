

if __name__ == '__main__':

    N, X, Y, Z = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    J = list(range(N))
    P =[]
    ans = []
    for i in range(N):
        P.append([-A[i], -B[i], -A[i]-B[i], i+1])

    # 数学の点でソート
    P = sorted(P, key=lambda x: (x[0], x[3]))

    for i in range(X):
        ans.append(P[0][3])
        P.pop(0)

    # 英語の点でソート
    P = sorted(P, key=lambda x: (x[1], x[3]))
    for i in range(Y):
        ans.append(P[0][3])
        P.pop(0)

    # 合計点でソート
    P = sorted(P, key=lambda x: (x[2], x[3]))
    for i in range(Z):
        ans.append(P[0][3])
        P.pop(0)

    for i in sorted(ans):
        print(i)




