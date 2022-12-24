

if __name__ == '__main__':
    # input
    N = int(input())
    T = list(map(int, input().split()))

    # 基準値設定
    T_sum = sum(T) # 答えになり得る最大値
    criteria = T_sum / 2 # 答えになり得る最小値

    # dp[i][j]: i個までの要素を使って合計jにできるかどうか（bool)
    dp = [[False]*(T_sum+1) for _ in range(N+1)]

    # 合計0にはできるのでj=0のときはTrueにする
    for i in range(N+1):
        for j in range(T_sum+1):
            dp[i][0] = True

    # dp
    for i in range(1, N+1):
        for j in range(1, T_sum+1):
            # T[i-1]個目の値を使わなくても、既にTrueの場合
            if dp[i-1][j]:
                dp[i][j] = True
                continue
            # T[i-1]を追加する前の値がTrueの場合、True
            if j-T[i-1] >= 0:
                dp[i][j] = dp[i-1][j-T[i-1]]

    # 全ての dp[i][j]==True について、jが基準以上かつ最小の値を求める
    ans = T_sum
    for i in range(N+1):
        for j in range(T_sum+1):
            if j >= criteria:
                if dp[i][j]:
                    ans = min(ans, j)

    print(ans)


