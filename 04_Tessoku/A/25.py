
if __name__ == '__main__':
    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        grid.append(input())

    # dp[i][j] : i行目j列目にいくパターン
    dp = [[0]*W for _ in range(H)]
    dp[0][0] = 1

    for i in range(H):
        for j in range(W):

            if grid[i][j] == '.':
                if j+1 < W:
                    if grid[i][j+1] == '.':
                        dp[i][j+1] += dp[i][j]
                if i+1 < H:
                    if grid[i+1][j] == '.':
                        dp[i+1][j] += dp[i][j]

    print(dp[H-1][W-1])











