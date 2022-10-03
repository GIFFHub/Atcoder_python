import math


def distance(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split())) # 明かりを持つ者
    B = [] # 明かりを持たぬ者
    for i in range(1, N+1):
        if i not in A:
            B.append(i)
    X = []
    Y = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    # 各明かりを持つ点から、明かりを持たない点への最短距離の最大値
    ans = 0
    for b in B:
        tmp = 10**12
        for a in A:
            # 特定の明かりから最も近い明かりでない点への距離
            tmp = min(tmp, distance([X[a-1], Y[a-1]], [X[b-1], Y[b-1]]))

        ans = max(ans, tmp)

    print(math.sqrt(ans))






