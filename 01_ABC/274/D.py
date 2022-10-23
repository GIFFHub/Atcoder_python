N, x, y = map(int, input().split())
A = list(map(int, input().split()))

# 奇数回目の移動はx軸方向
# 偶数回目の移動はy軸方向
# 奇数回目の移動を足し引きしてxにできるか
# 偶数回目の移動を足し引きしてyにできるか

A_x = []
A_y = []

flg = -1
x_pos = A[0]
y_pos = 0
for a in A:
    # 最初のAはA_xに入れない（正方向への移動とわかっているため）
    if flg == -1:
        flg = 1
        continue
    elif flg == 0:
        A_x.append(a)
        flg = 1
        continue
    else:
        A_y.append(a)
        flg = 0
        continue

# dp[i][j] : i番目までの移動で座標j-(dp_pos_size/2)にいることができるか
# dpで判定する座標は、移動し得る、-max(A)*N ~ max(A)*N
dp_x_pos_size = len(A_x) * max(A_x) * 2 + 1
dp_y_pos_size = len(A_y) * max(A_y) * 2 + 1

dp_x = [[False]*dp_x_pos_size for _ in range(0, len(A_x)+1)]
dp_y = [[False]*dp_y_pos_size for _ in range(0, len(A_y)+1)]

dp_x[0][dp_x_pos_size//2 + A[0]] = True
dp_y[0][dp_y_pos_size//2] = True

for i in range(1, len(A_y)+1):
    for j in range(dp_y_pos_size):
        if j-A_y[i-1] >= 0 and j+A_y[i-1] < dp_y_pos_size:
            dp_y[i][j] = dp_y[i-1][j-A_y[i-1]] or dp_y[i-1][j+A_y[i-1]]
        elif j-A_y[i-1] >= 0:
            dp_y[i][j] = dp_y[i-1][j-A_y[i-1]]
        elif j+A_y[i-1] < dp_y_pos_size:
            dp_y[i][j] = dp_y[i-1][j+A_y[i-1]]

for i in range(1, len(A_x)+1):
    for j in range(dp_x_pos_size):
        if j-A_x[i-1] >= 0 and j+A_x[i-1] < dp_x_pos_size:
            dp_x[i][j] = dp_x[i-1][j-A_x[i-1]] or dp_x[i-1][j+A_x[i-1]]
        elif j-A_x[i-1] >= 0:
            dp_x[i][j] = dp_x[i-1][j-A_x[i-1]]
        elif j+A_x[i-1] < dp_x_pos_size:
            dp_x[i][j] = dp_x[i-1][j+A_x[i-1]]

if x+(dp_x_pos_size//2) >= dp_x_pos_size or y+(dp_y_pos_size//2) >= dp_y_pos_size:
    print('No')
elif dp_x[len(A_x)][x+(dp_x_pos_size//2)] and dp_y[len(A_y)][y+(dp_y_pos_size//2)]:
    print('Yes')
else:
    print('No')









