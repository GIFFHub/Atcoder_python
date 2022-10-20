
def check_distance(xt, yt, xk, yk):
    d2 = (xt - xk) ** 2 + (yt - yk) ** 2
    if d2 == 5:
        return True
    else:
        return False


x1, y1, x2, y2 = map(int, input().split())

# (x1, y1)から距離が√5の格子点
Dx = [1, 2, 2, 1, -1, -2, -2, -1]
Dy = [2, 1, -1, -2, -2, -1, 1, 2]

for dx, dy in zip(Dx, Dy):
    if check_distance(x1 + dx, y1 + dy, x2, y2):
        print('Yes')
        break
else:
    print('No')
