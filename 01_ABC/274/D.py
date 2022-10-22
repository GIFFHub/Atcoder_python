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
    if flg == -1:
        flg = 1
    elif flg == 0:
        A_x.append(a)
        flg = 1
    else:
        A_y.append(a)
        flg = 0

A_x.sort(reverse=True)
A_y.sort(reverse=True)


for ax in A_x:
    if x_pos < x:
        x_pos += ax
    else:
        x_pos -= ax

for ay in A_y:
    if y_pos < y:
        y_pos += ay
    else:
        y_pos -= ay

if x_pos == x and y_pos == y:
    print('Yes')
else:
    print('No')


