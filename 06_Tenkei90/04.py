if __name__ == '__main__':
    H, W = map(int, input().split())
    A = []

    for _ in range(H):
        A.append(list(map(int, input().split())))

    A_x_sum = []
    for i in range(H):
        A_x_sum.append(sum(A[i]))

    A_y_sum = [0]*W
    for j in range(H):
        for k in range(W):
            A_y_sum[k] += A[j][k]

    ans = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            ans[i][j] = A_x_sum[i] + A_y_sum[j] - A[i][j]

    for a in ans:
        print(*a)




