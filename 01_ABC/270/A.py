def point(n):
    if n == 0:
        return [0,0,0]
    if n == 1:
        return [1,0,0]
    if n == 2:
        return [0,1,0]
    if n == 3:
        return [1,1,0]
    if n == 4:
        return [0,0,1]
    if n == 5:
        return [1,0,1]
    if n == 6:
        return [0,1,1]
    if n == 7:
        return [1,1,1]




A, B = map(int, input().split())

A_point = point(A)
B_point = point(B)

ans = 0
if A_point[0] or B_point[0] :
    ans += 1

if A_point[1] or B_point[1] :
    ans += 2

if A_point[2] or B_point[2] :
    ans += 4

print(ans)



