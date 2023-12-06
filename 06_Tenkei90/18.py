import math

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
E = [int(input()) for l in range(Q)]
P = math.pi
r = L / 2

# まず座標を出す
Xn = 0
Yn = 0
Zn = 0


def coordinate(e):
    pro = e / T
    phase = pro * 2 * P
    y = -1 * math.sin(phase) * r
    z = r - math.cos(phase) * r
    return [y, z]


for i in E:
    Yn = coordinate(i)[0]
    Zn = coordinate(i)[1]

    ab = math.sqrt((X) ** 2 + (Y - Yn) ** 2)
    print(math.degrees(math.atan(Zn / ab)))