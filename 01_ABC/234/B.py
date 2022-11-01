import math


def cal_distance(pos1: tuple, pos2: tuple) -> float:
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1]-pos2[1])**2)


if __name__ == '__main__':
    N = int(input())
    pos = []
    ans = 0
    for _ in range(N):
        x, y = map(int, input().split())
        pos.append((x, y))

    for p1 in pos:
        for p2 in pos:
            ans = max(ans, cal_distance(p1, p2))

    print(ans)

