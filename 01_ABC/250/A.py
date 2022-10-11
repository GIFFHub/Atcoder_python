H, W = map(int, input().split())
R, C = map(int, input().split())

left = (R-1, C)
right = (R+1, C)
up = (R, C+1)
down = (R, C-1)

pos = [left, right, up, down]
ans = 0
for p in pos:
    if 1 <= p[0] <= H and 1 <= p[1] <= W:
        ans += 1

print(ans)
