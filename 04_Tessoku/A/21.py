
# dp[l][r] : 一番左の番号がl-1, 一番右の番号がr-1の時の最大得点

N = int(input())

P = []
A = []
for _ in range(N):
    p, a = map(int, input().split())
    P.append(p)
    A.append(a)

dp = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N-1, -1, -1):

        # 左のブロック(i-1)を取り除いてきた場合
        point_left = 0
        if i >= 1:
            if i-1 <= P[i-1]-1 <= j:
                point_left += A[i-1]
        # 右のブロック(j+1)を取り除いてきた場合
        point_right = 0
        if j <= N-2:
            if i <= P[j+1]-1 <= j+1:
                point_right += A[j+1]

        if i == 0 and j == N-1: # 左も右も取り除いていない状態
            dp[i][j] = 0

        elif i == 0: # 左をまだ取り除いていない状態
            dp[i][j] = dp[i][j+1] + point_right

        elif j == N-1: # 右をまだ取り除いていない状態
            dp[i][j] = dp[i-1][j] + point_left

        else:
            dp[i][j] = max(dp[i-1][j] + point_left, dp[i][j+1] + point_right)

print(dp[N-1][0])


