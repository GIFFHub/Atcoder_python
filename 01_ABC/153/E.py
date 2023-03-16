

if __name__ == '__main__':
    H, N = map(int, input().split())
    for _ in range(N):
        a, b = map(int, input().split())

    # dp[i][j] i番目までの魔法を使って体力をj以下にする際の最大残り魔力


